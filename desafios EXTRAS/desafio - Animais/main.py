from rich import print,inspect
from animais import Cachorro, Gato

def main():
    c = Cachorro('Rex', 'Vira-lata')
    print(c.emitir_som())
    #inspect(c, methods=True)

    g = Gato('Frajola')
    print(g.emitir_som())
    #inspect(g, methods=True)

if __name__ == '__main__':
    main()