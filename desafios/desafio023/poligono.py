from abc import ABC, abstractmethod

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