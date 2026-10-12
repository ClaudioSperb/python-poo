class Termostato:
    def __init__(self, temperatura = 24):
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 24 <= valor <= 30 and valor % 0.5 == 0:
            self.__temperatura = valor
        else:
            raise ValueError('[ ERRO ], Coloque um valor Válido entre 24 e 30 °C\n'
                             'O Termostato funciona com intervalos de 0.5')


    def ftemperatura(self):
        return f'[blue b]{self.__temperatura}ºC[/]'
