from abc import ABC, abstractmethod # Abstract Base Classes

class Pessoa(ABC):
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversário(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de fazer a matricula')

    def estudar(self):
        print(f'O aluno {self.nome} esta estudando {self.curso} na turma {self.turma}')

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} começou a dar aula')

    def estudar(self):
        print(f'{self.nome} é especilsta em {self.especialidade} no {self.nivel}')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_pontos(self):
        print(f'O funcionario {self.nome} bateu o ponto')

    def estudar(self):
        print(f'{self.nome} se especializa para a área de {self.setor}')