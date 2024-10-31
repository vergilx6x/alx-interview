#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints."""
    skip = 0
    for byte in data:
        if skip:
            if byte >> 6 != 0b10:  # Check if the byte is a continuation byte
                return False
            skip -= 1
        else:
            if byte >> 7 == 0:      # 1-byte character (ASCII)
                continue
            elif byte >> 5 == 0b110:  # 2-byte character
                skip = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                skip = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                skip = 3
            else:
                return False
    return skip == 0
