from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto, salario):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        sal_min = 1612
        inss = 7.5

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        pass


class FuncionarioHorista:
    pass


class FuncionarioMensalista:
    pass