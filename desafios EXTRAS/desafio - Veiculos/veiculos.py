from rich import print, inspect
from rich.panel import Panel

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_dados(self):

        mensagem = (f'MARCA: {self.marca}\n'
                    f'MODELO: {self.modelo} \n')

        return mensagem


class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas

    def mostrar_dados(self):

        mensagem = (f'{super().mostrar_dados()}'
                    f'PORTAS: {self.qtd_portas} Portas')

        painel = Panel(mensagem, title='Dados do Veiculo', width=30, border_style='red')
        return painel


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def mostrar_dados(self):

        mensagem = (f'{super().mostrar_dados()}'
                    f'CILINDRADA: {self.cilindrada} cc')

        painel = Panel(mensagem, title='Dados do Veiculo', width=30, border_style='red')
        return painel

