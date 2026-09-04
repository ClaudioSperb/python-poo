from rich import print
from rich import inspect

#APRESENTAÇÃO FUNCIONÁRIO
class Funcionario:
    #Atributo de Classe
    empresa = 'Rek Reboques'

    # Método Construtor
    def __init__(self, nome, setor, cargo) -> str:

        #Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self):
        return (f'🤝 Sou [green]{self.nome}[/], trabalho no setor [red]{self.setor}[/] e meu cargo é \n[green]'
                f'{self.cargo}[/] na {Funcionario.empresa}')

c1 = Funcionario('Claudio', 'Comercial', 'Gerente')
print(c1.apresentação())
inspect(c1)

print('=-' * 35)

c2 = Funcionario('Josiane', 'Recepção', 'Recepcionista')
print(c2.apresentação())
inspect(c2)