from typing import Self

from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributos de Classe
    consumo_padrao:float = 0.400 # Cada pessoa com em media 400g de carne
    preco_kg:float = 82.40 # Cada Kg de carne custa $82.40

    def __init__(self, titulo, tot):
        #Atributos de Instância
        self.titulo = titulo
        self.participante = tot

    def __str__(self):
        return f"Esse é o {self.titulo} com {self.participante} pessoas participando."

    def calcular_qtd_carne(self) -> float:
        return self.participante * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participante

    def analisar(self):
        conteudo = f"Analisando [green b]{self.titulo}[/] com [b blue]{self.participante}[/] convidados"
        conteudo += (f"\nCada participante comerá {Churrasco.consumo_padrao} Kg e cada Kg custa R$"
                     f"{Churrasco.preco_kg:.2f}")
        conteudo += f"\nRecomendo comprar [blue]{self.calcular_qtd_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():.2f} reais[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():.2f}[/] reais para participar"
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco("Churras dos Amigos", 15)
c2 = Churrasco('Festa de Final de Ano', 10)
c1.analisar()
c2.analisar()