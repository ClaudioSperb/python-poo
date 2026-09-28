from abc import ABC, abstractmethod


class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = Moto.fator * self.distancia
        return f'R${self.frete:.2f}'


class Caminhao(Transporte):
    fator = 1.2

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return f'Raio minimo de 50Km não atingido'
        else:
            self.frete = Caminhao.fator * self.distancia
            return f'R${self.frete:.2f}'


class Drone(Transporte):
    fator = 9.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia > 10:
            self.frete = 0
            return f'Raio máximo de 10Km Ultrapassados'
        else:
            self.frete = Drone.fator * self.distancia
            return f'R${self.frete:.2f}'
