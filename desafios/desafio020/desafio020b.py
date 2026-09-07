from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favorito(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f'Nome Real: [black on white] {self.nome} [/]'
        conteudo += f'\nJogos Favoritos: '
        for num, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [blue b]{game}[/]'
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=50)
        print(painel)

j1 = Gamer('Claudio', 'MaxPain')
j1.add_favorito('Mario Bros')
j1.add_favorito('Sonic')
j1.add_favorito('Resident Evil')
j1.add_favorito('COD Mobile')
j1.ficha()

j2 = Gamer('Briana', 'Barbie')
j2.add_favorito('Jogo do Pato')
j2.add_favorito('Jogo do  Bebe')
j2.ficha()