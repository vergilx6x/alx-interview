#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else False."""
    skip = 0
    for byte in data:
        byte &= 0xFF  # Use only the least significant 8 bits
        if skip:
            if byte >> 6 != 0b10:
                return False
            skip -= 1
        else:
            # Determine the number of bytes in this character
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                skip = 1
            elif byte >> 4 == 0b1110:
                skip = 2
            elif byte >> 3 == 0b11110:
                skip = 3
            else:
                return False
    return skip == 0
