from rich import print, inspect

class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversário(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de fazer a matricula')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} começou a dar aula')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_pontos(self):
        print(f'O funcionario {self.nome} bateu o ponto')


a1 = Aluno('Claudio', 36, 'ADS', 'T01')
a1.fazer_aniversário()
a1.fazer_matricula()
inspect(a1)


p1 = Professor('Gustavo Guanabara', 45, 'T.I', 'Mestrado')
p1.dar_aula()
inspect(p1)

f1 = Funcionario('Claudio', 36, 'Gerente', 'Comercial')
f1.bater_pontos()
inspect(f1)