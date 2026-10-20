class Diario:
    def __init__(self, senha = 123):
        self.__segredos = []
        self.__senha = senha


    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(senha):
        pass