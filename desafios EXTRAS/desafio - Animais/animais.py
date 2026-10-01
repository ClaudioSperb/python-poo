from abc import ABC, abstractmethod

class Animais(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animais):

    def __init__(self, nome, raca):
        super().__init__(nome)
        self.nome = nome
        self.raca = raca

    def emitir_som(self):
        return f'o Cachorro 🐶 da raça [cyan b]{self.raca}[/] com nome [blue b]{self.nome}[/] latiu "Au-Au-Au"'


class Gato(Animais):

    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome

    def emitir_som(self):
        return f'O gato 🐈 com nome [red b]{self.nome}[/] fez "Miau-Miau"'