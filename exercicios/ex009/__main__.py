from ex009 import Avaliacao
from rich import print, inspect


def main():
    av1 = Avaliacao("Claudio", "Matemática")
    #av1.nota = -345
    inspect(av1, private=True)

if __name__ == '__main__':
    main()