from rich import print

class Caneta:
    def __init__(self, nome_cor):
        self.destampado = True
        self.quebra_linha = False
        self.cor = nome_cor.lower()
        if self.cor == 'vermelho':
            self.cor = 'red'
        elif self.cor == 'verde':
            self.cor = 'green'
        elif self.cor == 'azul':
            self.cor = 'blue'

    def escrever(self, msg):
        if self.destampado:
            print(f"[b {self.cor}] {msg} [/]")

    def quebrar(self, num=1):
        self.quebra_linha = True
        for i in range(num):
            print('=-' * 30)

    def destampar(self):
        self.destampado = False
        print(f'⚠️ [on red]A caneta {self.cor} esta tampada[/]')

p1 = Caneta('Vermelho')
p1.destampar()
p1.escrever('Testando cores em PYTHON POO')
p1.quebrar(5)

p2 = Caneta('verde')
p2.destampar()
p2.escrever('Testando cores em PYTHON POO')


