from forma_geometrica import *
from rich import print


def main():
    q1 = Quadrado(5)
    print(f'AREA DO [red b]{Quadrado.__name__.upper()}:[/] {q1.calcular_area()} cm²')
    print(f'PERIMETRO DO [red b]{Quadrado.__name__.upper()}:[/] {q1.calcular_perimetro()} cm')

    print('=-' * 15)

    r1 = Retangulo(5, 2)
    print(f'AREA DO [red b]{Retangulo.__name__.upper()}:[/] {r1.calcular_area()} cm²')
    print(f'PERIMETRO DO [red b]{Retangulo.__name__.upper()}:[/] {r1.calcular_perimetro()} cm')
if __name__ == '__main__':
    main()