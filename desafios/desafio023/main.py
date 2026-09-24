from poligono import *
from rich import print, inspect

def main():
    p1 = Quadrado(10)

    print(f'Area = {p1.area():.2f}')
    print(f'Perimetro = {p1.perimetro():.2f}')
    #inspect(p1, methods=True)

if __name__ == '__main__':
    main()