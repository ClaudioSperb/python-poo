#Criando uma Classe
class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        return f'{self.nome} esta Latindo!'
#Criando o objeto a partir da Classe Cachorro
meu_cachorro = Cachorro('Rex')
print(meu_cachorro.latir())