from abc import ABC, abstractmethod
from rich import print

class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print('--- 🏁 Iniciando Preparo 🏁 ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('--- ✅  Bebida Pronta ✅  ---')

    def ferver_agua(self):
        print(f'1. 🔥 Fervendo a água em 100º Celcius 🔥')

    @abstractmethod
    def misturar(self):
        pass

    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        print(f'2. 🔜 Passando água pressurizada pelo pó de café moído')

    def servir(self):
        print(f'3. 🔜 Servindo em uma xícara pequena')


class Leite(BebidaQuente):

    def misturar(self):
        print(f'2. 🥛 Passando vapor pressurizado pelo bico do leite 🥛')

    def servir(self):
        print(f'3. ☕  Servindo na caneca Grande, já com o café ☕ ')


class Cha(BebidaQuente):
    def misturar(self):
        print(f'2. 🫗 Mergulhando o sachê de ervas na água 🫖')

    def servir(self):
        print(f'3. 🫖 Servindo na caneca de porcelana com limão 🍵')