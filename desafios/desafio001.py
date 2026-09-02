from rich import print

#APRESENTAÇÃO FUNCIONÁRIO
class Funcionario:
    def __init__(self, nome, setor, cargo): #Método Construtor

        #Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self):
        return f'🤝 Sou [green]{self.nome}[/], trabalho no setor [red]{self.setor}[/] e meu cargo é \n[green]{self.cargo}[/] na REK REBOQUES!'

c1 = Funcionario('Claudio', 'Comercial', 'Gerente')
print(c1.apresentação())

print('=-' * 35)

c2 = Funcionario('Josiane', 'Recepção', 'Recepcionista')
print(c2.apresentação())
