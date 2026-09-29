from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

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
        base = self.salario / Funcionario.sal_min

        mensagem = (f'O salário de [blue b]{self.nome}[/] ([magenta b]{self.__class__.__name__}[/]) é de [green b]R'
                    f'${self.salario:.2f}[/] e '
                    f'corresponde a'
                    f' [yellow b]{base:.1f} salários '
                    f'minimos[/]')
        painel = Panel(mensagem, title='Analise de Salario', width=50)
        print(painel)



class FuncionarioHorista(Funcionario):

    def __init__(self, nome, valor_hora = 7.37, qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_horas
        self.sal_bruto = self.valor_hora * self.horas_trabalhadas

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)



class FuncionarioMensalista(Funcionario):

    def __init__(self, nome, sal_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)