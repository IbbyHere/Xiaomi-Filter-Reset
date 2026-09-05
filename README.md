# Xiaomi Filter Reset

Generates the reset code for a **Xiaomi Mi Air Purifier 4** filter's NFC tag
from the filter's UID, so its "remaining life" counter can be reset to 100%.

**Live tool:** https://ibbyhere.github.io/Xiaomi-Filter-Reset/

## Why

The filter's NFC tag tracks usage on a fixed schedule, not actual filter
condition, so the Mi Home app often demands a replacement long before the
filter is actually spent. This lets you reset the counter on a filter you've
inspected and judged still good.

This is an unofficial, community reverse-engineered method (credit to
[Unethical Info](https://unethical.info/2024/01/24/hacking-my-air-purifier/)
and Flamingo-tech), not affiliated with or supported by Xiaomi. The same
NFC scheme is also used on other Mi Air Purifier models (2S, 3H, Pro, Pro H,
Elite, 4 Lite, 4 Pro), so this should work for those too.

## How it works

The filter's UID (14 hex characters) is SHA-1 hashed, and four bytes from fixed
positions in the hash are used to build a password. The full reset command
sent to the tag is `1B<password>,3008,A20800000000` — a raw NFC-A command
sequence: authenticate with the password, then write zero to the usage
counter's memory page.

## Flashing the tag (Android + NFC Tools)

1. Install the free **NFC Tools** app (by wakdev) from the Play Store on an
   NFC-capable Android phone.
2. Open NFC Tools, tap **Read**, then hold your phone against the filter's
   NFC tag until it scans. Note the **UID / Serial number** shown (14 hex
   characters).
3. Enter that UID into the live tool (or run `main.py`) to get the reset
   command.
4. In NFC Tools, go to **Other > Advanced NFC commands**, then tap **accept**
   on the warning.
5. Set the I/O class to `NfcA (ISO 14443-3A)`.
6. Paste the generated reset command (e.g. `1B...,3008,A20800000000`) into
   the data box.
7. Hold your phone against the filter's tag again and tap **Send command**.
8. Reopen the Mi Home app — the filter should now show 100% remaining life.

**Note:** this resets the app's counter, not the physical filter — only do
this for a filter you believe is still good.

## Usage

- **Browser:** open `index.html` (or the live tool link above) and enter the UID.
- **CLI:** `python main.py` and enter the UID when prompted.
