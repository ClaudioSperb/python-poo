from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, lado):
        self.lado = lado

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__(lado)

    def calcular_perimetro(self):
        perimetro = self.lado * 4
        return perimetro

    def calcular_area(self):
        area = self.lado ** 2
        return area


class Retangulo(FormaGeometrica):
    def __init__(self, lado, altura):
        super().__init__(lado)
        self.altura = altura

    def calcular_perimetro(self):
        perimetro = self.lado * 2 + self.altura * 2
        return perimetro

    def calcular_area(self):
        area = self.lado * self.altura
        return area