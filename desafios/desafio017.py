from rich.panel import Panel
from rich import print

#CRIANDO ETIQUETAS

class Produto:

    """
    Classe que adiciona um produto e um valor
    """

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):

        """
        Metodo criado para criar uma etiqueta
        :return: Uma etiqueta com o nome do Produto e o valor do produto
        """

        real = f'R${self.preco:.2f}'.replace('_', '.').replace('.',',')
        caixa = Panel(f'[blue b]{self.nome:^32}[/] \n [green b]{29 * '~'}[/] \n[white b]{real:^32}[/]',title='PRODUTO',
                      width=35,style='red')
        print(caixa)

p1 = Produto('Celular', 2_000.00)
p1.etiqueta()

p2 = Produto('NoteBook', 5_500.00)
p2.etiqueta()

p3 = Produto('Casa Propria', 150_000.00)
p3.etiqueta()