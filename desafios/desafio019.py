class Livro:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.pag = paginas

    def avançar_pagina(self):
        for c in range(self.pag):
            print(f'{c + 1}', end=' ')
        print(c + 1)


l1 = Livro('Teste', 5)
l1.avançar_pagina()