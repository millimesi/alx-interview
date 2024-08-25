#!/usr/bin/python3
""" utf-8 validation """


def validUTF8(data):
    """
    validate utf emcoding
    """
    bytes_count = 0
    m1 = 1 << 7
    m2 = 1 << 6

    for byte in data:
        if bytes_count == 0:
            mask = 1 << 7
            while mask & byte:
                bytes_count += 1
                mask >>= 1
            if bytes_count == 0:
                continue

            if bytes_count == 1 or bytes_count > 4:
                return False
        else:
            if not (byte & m1 and not (byte & m2)):
                return False

        bytes_count -= 1

    return bytes_count == 0
