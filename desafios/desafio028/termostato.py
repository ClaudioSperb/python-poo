class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError('[ ERRO ], Coloque um valor Válido entre 24 e 30 °C\n'
                             'O Termostato funciona com intervalos de 0.5')
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor


    def ftemperatura(self):
        return f'[blue b]{self.__temperatura}ºC[/]'
