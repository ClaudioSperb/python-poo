from rich import print
from rich import inspect

#Exercio que simula uma conta Bancária
class ContaBancaria:
    """
    Cria uma Conta Bancaria e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        print(f'\033[32mConta {id} criado com sucesso\033[0m | Saldo atual: {self.saldo:.2f}')
        print('=-' * 25)

    def __str__(self):
        return f'Conta -> {self.id} | Usuário -> {self.nome} | Saldo -> R${self.saldo:.2f}'


    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito: R$ {self.saldo:.2f} | ID do Usuário: {self.id}')
        print('\033[32mDepósito efetuado com Sucesso!\033[0m')
        print('=-' * 25)

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'\033[31mSaque NEGADO!\033[0m - Saldo Insuficiente!')
        else:
            self.saldo -= valor
            print(f'Saque de: {valor:.2f} | da conta con ID: {self.id} | Saldo atual: {self.saldo:.2f}')
            print('\033[32mSaque efetuado com Sucesso!\033[0m')
            print('=-' * 25)

c1 = ContaBancaria(1, 'Claudio', 1000)
inspect(c1)
