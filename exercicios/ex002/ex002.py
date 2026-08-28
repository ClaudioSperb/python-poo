#Declaração de Classe
class Gafanhoto:
    """
    Cria um objeto Gafanhoto que tem como atributos, nome e idade.
    variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, nome='vazio', idade=0): #Método Construtor
        #Atributos de Instância
        self.nome = nome
        self.idade = idade

    #Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1


    def __str__(self): #DUNDER METHOD
        if self.nome == 'vazio' and self.idade == 0:
            return 'Nenhum dado informado'
        else:
            return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        if self.nome == 'vazio' and self.idade == 0:
            return 'Variável sem nenhum dado'
        else:
            return f'Estado: nome = {self.nome}; idade = {self.idade}'

#Declaração de Objetos
g1 = Gafanhoto("Claudio", 36) #Objeto criado usando a classe Gafanhoto()
g1.aniversario()
print(g1)

print(g1.__doc__) #Docstring / DUNDER ATTRIBUTE
print(g1.__dict__) # Atributo
print(g1.__getstate__()) #Método
print(g1.__class__)
