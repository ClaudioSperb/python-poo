from time import sleep
from rich import print

class Livro:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.pag = paginas
        self.pagina_inicial = 1

    def avançar_pagina(self, avancar):
        tot_pag = avancar + self.pagina_inicial
        for c in range(self.pag):
            print(f'Pag{c + 1}➡️', end=' ')
            sleep(0.5)
        avancar += tot_pag

l1 = Livro('Teste', 5)
l1.avançar_pagina(5)
l1.avançar_pagina(2)