from frete import *
from rich import print

def main():
    dist = 80

    entrega = Drone(dist)

    print(f'Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete():.2f}')


if __name__ == '__main__':
    main()