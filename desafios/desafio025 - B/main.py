from transportes import *
from rich import print

def main():
    dist = 5
    entrega = Drone(dist)
    print(f'Frete de {entrega.__class__.__name__} com {dist}Km = {entrega.calcular_frete()}')


if __name__ == '__main__':
    main()