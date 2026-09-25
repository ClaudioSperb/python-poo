from frete import *
from rich import print

def main():
    dist = 50

    entrega = Drone(dist)

    print(f'Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}')


if __name__ == '__main__':
    main()