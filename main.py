import hashlib
import re


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