#Declaração de Classe
class Gafanhoto:
    def __init__(self): #Método Construtor
        #Atributos de Instância
        self.nome = ''
        self.idade = 0

    #Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

#Declaração de Objetos
g1 = Gafanhoto() #Objeto criado usando a classe Gafanhoto()
g1.nome = 'Claudio'
g1.idade = 36
g1.aniversario()
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Cristen'
g2.idade = 24
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = 'Josiane'
g3.idade = 25
g3.aniversario()
print(g3.mensagem())