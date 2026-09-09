from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min = int(1)
    canal_max = int(6)
    volume_min = int(1)
    volume_max = int(5)

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual = int(canal)
        self.volume_atual = int(volume)
        self.ligado = bool(False)

    def liga_desliga(self):
        self.ligado = not self.ligado

    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f':prohibited: [red b]A TV está desligada[/]'
        else:
            conteudo = f'CANAL  ='
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f' [black on yellow] {canal} [/] '
                else:
                    conteudo += f' {canal} '

            conteudo += f'\nVOLUME = '
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f'[black on cyan]   [/]'
                else:
                    conteudo += f'[black on white]   [/]'

        tv = Panel(conteudo, title='[ TV ]', width=33)
        print(tv)


c = ControleRemoto(6, 6)
c.liga_desliga()
c.mostrar_tv()