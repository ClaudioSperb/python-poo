from abc import ABC, abstractmethod

class Funcionario(ABC):

    sal_min = 1612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        pass



class FuncionarioHorista(Funcionario):

    def __init__(self, nome, valor_hora = 7.37, qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_horas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas

    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.valor_hora * Funcionario.inss / 100)


class FuncionarioMensalista(Funcionario):

    def __int__(self):
        super().__init__()


    def calcular_salario(self):
        pass