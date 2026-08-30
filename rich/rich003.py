from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Valores")
tabela.add_column("Produto", justify="left", width=20)
tabela.add_column("Valor", justify="center")

tabela.add_row("Celular", 'R$2.000,00')
tabela.add_row("Notebook", 'R$3.500,00')

print(tabela)