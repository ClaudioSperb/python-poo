from rich.panel import Panel
from rich import print

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_jogo_favorito(self, jogo_favorito):
        self.jogos.append(jogo_favorito)
        self.jogos.sort()

    def mostrar_jogos(self):
        for jogo in self.jogos:
            print(jogo)

    def tabela_jogador(self):
        jogos_formatados = "\n".join(f"-🎮 {jogo}" for jogo in self.jogos)
        painel_jogador = Panel(f'Nome Real: [on red b] {self.nome:>10} [/]\n'
                               f'Jogos Favoritos: \n'
                               f'{18 * '=-'}\n'
                               f'[green]{jogos_formatados}[/]',title=self.nick, width=40)
        print(painel_jogador)



j1 = Gamer(nome='Claudio Sperb', nick='Jogador 1')
j1.add_jogo_favorito('Mario Bross')
j1.add_jogo_favorito('Resident Evil')
j1.add_jogo_favorito('Naruto')
j1.tabela_jogador()

j2 = Gamer(nome='Josiane Segatto', nick='Jogador 2')
j2.add_jogo_favorito('Jogo 1')
j2.add_jogo_favorito('Jogo 2')
j2.add_jogo_favorito('Jogo 3')
j2.add_jogo_favorito('Jogo 4')
j2.tabela_jogador()

j3 = Gamer(nome='Briana Segatto', nick='Jogador 3')
j3.add_jogo_favorito('Jogo 1')
j3.add_jogo_favorito('Jogo 2')
j3.add_jogo_favorito('Jogo 3')
j3.add_jogo_favorito('Jogo 4')
j3.tabela_jogador()
