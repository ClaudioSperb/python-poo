from abc import ABC, abstractmethod
from rich import print
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]

            print(f'[blue b]{self.nome}[/]({self.vida}) 🚨 Fez um ATAQUE em 🚨 => [green b]{alvo.nome}[/] ({alvo.vida}) '
                  f'com o '
                  f'golpe [magenta b'
                  f']{golpe}[/] com força {forca}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer')

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"[purple b]{self.nome}[/] recebeu dano de ☠️ [red b] -{fator}[b] ☠️")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco 👊', 'Golpe de Machado 🪓', 'Pulo giratório 🌪️' ]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue b]{self.nome}[/] usou um kit medico e [green b]recuperou {fator} pontos de Vida[/]')


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo 🔥', 'Raio de Luz ⚡', 'Magia Estática 🪄']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue b]{self.nome}[/] usou uma poção mágiva e [green b]recuperou {fator} pontos de Vida[/]')
