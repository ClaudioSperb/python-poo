from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        frete = self.distancia * 0.5
        frete = float(frete)
        return frete

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            return '[ERRO] - Raio inferior a 50Km'
        else:
            frete = self.distancia * 1.20
            frete = float(frete)
            return frete

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia >= 11:
            return '[ERRO] - Raio de 10Km Ultrapassados!'
        else:
            frete = self.distancia * 9.50
            frete = float(frete)
            return frete