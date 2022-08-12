
from cesar import cesar
from itertools import cycle


def vigenere(text, key, encode=True):
    """
    Returns the text encryption <text> by the <key>
    The <key>'s characters must be some ASCII alphabetic characters
    """
    return "".join(cesar(k, v, encode) for k, v in zip(text, cycle(key)))
