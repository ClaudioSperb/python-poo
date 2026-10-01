from rich import print
from rich.panel import Panel

class Funcionario:
    bonificacao = 10
    def __init__(self, nome, salario, vendas):
        self.nome = nome
        self.salario = salario
        self.vendas = vendas

    def mostrar_dados(self):
        mensagem = (f'NOME: {self.nome}\n'
                    f'SALARIO: {self.salario:.2f}\n'
                    f'VENDAS: {self.vendas} vendas')
        analise = Panel(mensagem, title=f'Tabela - {self.nome}',width=30, border_style='red')
        print(analise)


class Gerente(Funcionario):
    def __init__(self, nome, salario, vendas):
        super().__init__(nome, salario, vendas)
        self.vendas = vendas

    def bonus(self):
        if self.vendas > 10:
            valor_salario_bonus = self.salario * (Funcionario.bonificacao / 100) + self.salario
            print(f'O funcionario {self.nome} aingiu a meta e [green b]ganhou 10%[/] a mais - Salario do mes '
                    f'- [green b]R${valor_salario_bonus} reais[/]')
        else:
            print(f'O funcuinario {self.nome} nao atingiu a meta da bonificação - Salario do mes - [blue b]R'
                    f'${self.salario} reais[/]')

class Programador(Funcionario):
    def __init__(self, nome, salario, vendas, linguagem):
        super().__init__(nome, salario, vendas)
        self.linguagem = linguagem

    def mostrar_dados(self):
        mensagem = (f'NOME: {self.nome}\n'
                    f'SALARIO: {self.salario:.2f}\n'
                    f'LINGUAGEM: {self.linguagem}')
        analise = Panel(mensagem, title=f'Tabela - {self.nome}', width=30, border_style='red')
        print(analise)

