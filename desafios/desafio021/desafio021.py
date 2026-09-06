from rich import print

class Caneta:
    def __init__(self, nome_cor):
        self.cor = nome_cor.lower()
        if self.cor == 'vermelho':
            self.cor = 'red'
        elif self.cor == 'verde':
            self.cor = 'green'
        elif self.cor == 'azul':
            self.cor = 'blue'

    def escrever(self, msg):
            print(f"[{self.cor}] {msg} [/]")


p1 = Caneta('Vermelho')
p1.escrever('Testando cores em PYTHON POO')


