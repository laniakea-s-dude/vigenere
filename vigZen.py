
from vigenere import vigenere
import this


def vig_zen(key=input("\n==============\nHit your key :\n\n"),
            encode=True):

    """ A joke to transcript this.s with vigenere code and a chosen key """

    print(f"==========\nRow this.s :\n==========\n{this.s}")

    print(f"\n====================================================="
          f"\nthis.s transcription with vigenere code by your key :"
          f"\n======================================================\n\n"
          f"{vigenere(this.s, key, encode)}")


vig_zen()
