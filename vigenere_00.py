
import string
from itertools import cycle


class Vigenere:

    def __int__(self):
        pass

    def encode_decode(self, text, key, encode=True):
        self.text = text
        self.key = key
        self.encode = encode

        def cesar(clear, clave):
            # encode = self.encode
            if clear not in string.ascii_letters:
                return clear
            # clave_value is the offset value, for example "c" mean an offset of 3
            clave_value = ord(clave.lower()) - 96
            if not self.encode:
                clave_value *= - 1
            bottom = 65 if clear.isupper() else 97
            return chr(bottom + (ord(clear) - bottom + clave_value) % 26)

        return "".join(cesar(cle, cla)
                       for cle, cla in zip(self.text, cycle(self.key)))
