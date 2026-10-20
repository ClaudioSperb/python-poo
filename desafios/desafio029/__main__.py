from diario_secreto import *
from rich import print, inspect

def main():
    d = Diario()
    d.escrever('Testando a lista')
    d.escrever('Teste 2')
    d.escrever('Teste 3')

    inspect(d, methods=True, private=True)


if __name__ == '__main__':
    main()