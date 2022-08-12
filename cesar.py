
import string


def cesar(clear, key, encode=True):
    """
    Returns the character encryption <clear> by the <key>
    The <key> character must be an ASCII alphabetic character
    """
    if clear not in string.ascii_letters:
        return clear
    # key_value is the offset value, for example "c" mean an offset of 3
    key_value = ord(key.lower()) - 96

    if not encode:
        key_value *= - 1

    bottom = 65 if clear.isupper() else 97

    return chr(bottom + (ord(clear) - bottom + key_value) % 26)
