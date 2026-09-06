from time import sleep
from rich import print

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.total_paginas}[/] paginas no total. Você agora está na [yellow]pagina {self.pagina_atual}[/yellow][/blue]")

    def avancar_paginas(self, qtd_paginas = 1):
        cont = 0
        for pg in range(0, qtd_paginas, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end="")
                sleep(0.3)
                cont += 1
        print(f"[blue]Você avançou {cont} paginas e esta na [yellow]página {self.pagina_atual}[/][/blue]")
        if self.fim_do_livro():
            print(f":closed_book: Você chegou no fim do Livro [green]'{self.titulo}'[/]:")

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False

l1 = Livro('Livro 01', 20)
l1.avancar_paginas(10)
l1.avancar_paginas(5)
l1.avancar_paginas(10)