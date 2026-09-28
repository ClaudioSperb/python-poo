from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto, salario):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        sal_min = 1612
        inss = 7.5


    def analisar_salario(self):
        pass

    @abstractmethod
    def calcular_salario(self):
        pass


class FuncionarioHorista(Funcionario):

    def __init__(self, nome, sal_bruto, salario):
        super().__init__(nome, sal_bruto, salario)

    def valor_hora(self):
        pass

    def horas_trabalhadas(self):
        pass

    def calcular_salario(self):
        pass

class FuncionarioMensalista(Funcionario):

    def __init__(self, nome, sal_bruto, salario):
        super().__init__(nome, sal_bruto, salario)

    def calcular_salario(self):
        pass