import hashlib
import re

# Xiaomi Filter Reset
#
# What this is:
# The filter's NFC tag counts down on a timer, it does not actually check
# how dirty the filter is. So the Mi Home app keeps telling you to buy a
# new filter even when it is still fine. This script generates the code
# needed to reset that counter back to 100%.
#
# What it's for:
# Made for the Xiaomi Mi Air Purifier 4. Should also work on the 2S, 3H,
# Pro, Pro H, Elite, 4 Lite and 4 Pro since they use the same tag.
#
# How to use this script:
# 1. Run this script (python main.py) and enter the filter's 14 character
#    UID when asked. It will print a "Code" and a "Reset command".
#
# How to flash the tag (Android + NFC Tools app):
# 1. Install the free NFC Tools app from the Play Store.
# 2. Open the app, tap Read, and hold the phone on the filter's tag.
#    Write down the UID / Serial number shown (14 hex characters).
# 3. Enter that UID into this script to get the reset command.
# 4. In NFC Tools go to Other, then Advanced NFC commands, and accept
#    the warning.
# 5. Set the I/O class to NfcA (ISO 14443-3A).
# 6. Paste in the whole reset command that this script printed out.
# 7. Hold the phone on the tag again and press Send command.
# 8. Open the Mi Home app, the filter should now show 100%.
#
# Disclaimer:
# Only do this on a filter that has been checked and is still ok to use.
# This only resets what the app says, it does not clean the filter.
# Writing to the tag could fail sometimes, so do this at your own risk.


def generate_code(uid):
    # Remove spaces and other characters from the UID
    uid = re.sub(r"[^0-9A-Fa-f]", "", uid)

    # Check that the UID is the correct length
    if len(uid) != 14:
        raise ValueError("The UID must contain 14 hexadecimal characters.")

    # Convert the UID from hexadecimal into bytes
    uid_bytes = bytes.fromhex(uid)

    # Create a SHA-1 hash from the UID
    hash_value = hashlib.sha1(uid_bytes).digest()

    # Use the first byte to choose which parts of the hash to use
    start = hash_value[0]

    positions = [
        start % 20,
        (start + 5) % 20,
        (start + 13) % 20,
        (start + 17) % 20
    ]

    # Get the four bytes and convert them to hexadecimal
    code = ""

    for position in positions:
        code += f"{hash_value[position]:02X}"

    return code


def main():
    # Ask the user for the UID
    uid = input("Enter the filter UID: ").strip()

    try:
        code = generate_code(uid)

        # Create the reset command
        command = f"1B{code},3008,A20800000000"

        print("\nCode:", code)
        print("Reset command:", command)

    except ValueError as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()