from rich import inspect
from personagens_rpg import *


def main():
    p1 = Guerreiro('Goku', 2000)
    p2 = Mago('Mago Negro', 2500)

    p1.atacar(p2, 500)
    inspect(p1, methods=True)
    #inspect(p2, methods=True)

    p1.receber_dano(100)
    inspect(p1)

if __name__ == '__main__':
    main()