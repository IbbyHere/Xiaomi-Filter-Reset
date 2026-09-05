# Xiaomi Filter Reset

Generates the reset code for a Xiaomi Mi Air Purifier 4 filter's NFC tag,
so you can reset the "remaining life" counter back to 100%.

**Live tool:** https://ibbyhere.github.io/Xiaomi-Filter-Reset/

## Why this exists

The filter's NFC tag just counts down on a timer, it doesn't actually check
how dirty the filter is. So the Mi Home app will keep nagging you to buy a
new filter even if yours is still perfectly fine. This lets you reset the
counter on a filter you've checked out and are happy to keep using.

Same tag scheme is used on the 2S, 3H, Pro, Pro H, Elite, 4 Lite and 4 Pro
too, so it should work on those as well.

## How it works

Take the filter's UID (14 hex characters), SHA-1 hash it, and pull four
bytes out of fixed spots in that hash to build a password. The full reset
command sent to the tag ends up being `1B<password>,3008,A20800000000`,
which is really just: authenticate with the password, then write zero over
the usage counter's memory page.

## Flashing the tag (Android + NFC Tools)

1. Grab the free NFC Tools app (by wakdev) from the Play Store. Needs an
   NFC-capable Android phone.
2. Open it, tap Read, and hold your phone against the tag on the filter
   until it picks it up. Note the UID / Serial number it shows (14 hex
   characters).
3. Pop that UID into the live tool (or `main.py`) to get your reset
   command.
4. In NFC Tools, go to Other > Advanced NFC commands and accept the
   warning.
5. Set the I/O class to `NfcA (ISO 14443-3A)`.
6. Paste in the whole reset command you just generated.
7. Hold your phone up to the tag again and hit Send command.
8. Open Mi Home back up, filter should now read 100%.

Only do this on a filter you've actually checked and think is still good.
It resets what the app thinks, it doesn't clean or extend the actual
filter.

## Usage

- **Browser:** open `index.html` (or the live tool link above) and enter the UID.
- **CLI:** `python main.py` and enter the UID when prompted.
