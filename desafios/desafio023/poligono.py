from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, lado):
        self.lado = lado

    @abstractmethod
    def area(self):
       pass

    def perimetro(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(lado)

    def area(self):
        area = self.lado ** 2
        return area

    def perimetro(self):
        perimetro = self.lado * 4
        return perimetro

class Circulo(Poligono):
    def __init__(self, lado):
        super().__init__(lado)

    def area(self):
        area_circulo = pi * (self.lado ** 2)
        return area_circulo

    def perimetro(self):
        perimetro_circulo = 2 * pi * self.lado
        return perimetro_circulo


class Triangulo(Poligono):
    def __init__(self, lado):
        super().__init__(lado)


    def area(self):
        area_triangulo = self.lado * self.lado / 2
        return area_triangulo

    def perimetro(self):
        perimetro_triangulo = self.lado * 3
        return perimetro_triangulo

