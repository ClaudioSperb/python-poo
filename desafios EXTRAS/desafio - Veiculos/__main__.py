from rich import inspect, print
from veiculos import *

def main():
    carro = Carro('Fiat', 'Uno', 4)
    #inspect(c, methods=True)
    print(carro.mostrar_dados())

    carro2 = Carro('Chevrolet', 'Onix Sedan', 4)
    print(carro2.mostrar_dados())

    moto = Moto('Yamaha', 'Fazer', 250)
    print(moto.mostrar_dados())
    #inspect(moto)

    moto2 = Moto('Honda', 'Fan 160', 160)
    print(moto2.mostrar_dados())

if __name__ == '__main__':
    main()