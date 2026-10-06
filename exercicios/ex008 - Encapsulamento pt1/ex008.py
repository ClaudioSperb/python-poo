#Exercio que simula uma conta Bancária
class ContaBancaria:
    """
    Cria uma Conta Bancaria e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id # Publico ( + )
        self._nome = nome # Protegido ( # )
        self.__saldo = saldo # Privado ( - )
        print(f'\033[32mConta {id} criado com sucesso\033[0m | Saldo atual: {self.__saldo:.2f}')
        print('=-' * 25)

    def __str__(self):
        #return f'Conta -> {self.id} | Usuário -> {self.nome} | Saldo -> R${self.__saldo:.2f}'
        return f'Estado atual da conta: {self.__dict__}'


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito: R$ {self.__saldo:.2f} | ID do Usuário: {self.id}')
        print('\033[32mDepósito efetuado com Sucesso!\033[0m')
        print('=-' * 25)

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'\033[31mSaque NEGADO!\033[0m - Saldo Insuficiente!')
        else:
            self.__saldo -= valor
            print(f'Saque de: {valor:.2f} | da conta con ID: {self.id} | Saldo atual: {self.__saldo:.2f}')
            print('\033[32mSaque efetuado com Sucesso!\033[0m')
            print('=-' * 25)