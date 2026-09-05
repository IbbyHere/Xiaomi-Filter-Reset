# Xiaomi Filter Reset

Generates the reset code for Xiaomi water filter NFC tags from the filter's UID.

**Live tool:** https://ibbyhere.github.io/Xiaomi-Filter-Reset/

## How it works

The filter's UID (14 hex characters) is SHA-1 hashed, and four bytes from fixed
positions in the hash are used to build the reset code. The reset command sent
to the filter tag is `1B<code>,3008,A20800000000`.

## Usage

- **Browser:** open `index.html` (or the live tool link above) and enter the UID.
- **CLI:** `python main.py` and enter the UID when prompted.
