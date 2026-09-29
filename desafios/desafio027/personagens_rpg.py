from abc import ABC, abstractmethod
from rich import print
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        if self.vida >0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]

            print(f'[blue b]{self.nome}[/] 🚨 Fez um ATAQUE em 🚨 => [green b]{alvo.nome}[/] com o golpe [magenta b'
                  f']{golpe}[/]')

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu dano de ☠️ [red b] -{fator}[b] ☠️")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco 👊', 'Golpe de Machado 🪓', 'Pulo giratório 🌪️' ]

    def curar(self):
        pass


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo 🔥', 'Raio de Luz ⚡', 'Magia Estática 🪄']

    def curar(self):
        pass
