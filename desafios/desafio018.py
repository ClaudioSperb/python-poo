from rich.panel import Panel
from rich import print

#LISTA DE CHURRASCO
#Consumo por pessoa = 400g
#preço do Kg da Carne = $82.40/Kg

class Churrasco:
    #Atrbutos de Classe
    consumo_padrao = 0.400
    preco_kg = 82.40

    def __init__(self, titulo, tot):
        self.titulo = titulo
        self.tot = tot

    def analisar(self):
        #Variaveis para os calculos
        recomendacao = 0.4 * self.tot
        custo_total = 82.40 * recomendacao
        div_pessoa = custo_total / self.tot

        caixa = Panel(f'Analisando [green b]{self.titulo}[/] com [blue b]{self.tot}[/] convidados\n'
                      f'Cada convidado consumirá {Churrasco.consumo_padrao}Kg e o preço por Kg é {Churrasco.preco_kg}\n'
                      f'Recomendamos comprar [blue b]{recomendacao:.3f}Kg[/] de carne no total !\n'
                      f'O valor total do Churrasco é de [green b]R${custo_total:.2f}[/] reais !\n'
                      f'Valor por pessoa do Churrasco é [yellow b]R${div_pessoa:.2f}[/] reais!',
                      title=self.titulo,width=100)
        print(caixa)

c1 = Churrasco('Churras dos Amigos', 500)
c1.analisar()