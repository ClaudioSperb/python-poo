from ex010 import Avaliacao
from rich import print, inspect


def main():
    av1 = Avaliacao("Claudio", "Matemática")
    av1.nota = 9888
    print(f'{av1.nome} tirou {av1.nota} em {av1.disciplina}')
    #inspect(av1, private=True) #private=True faz mostrar os atributos privados

if __name__ == '__main__':
    main()