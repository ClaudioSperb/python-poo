from termostato import Termostato
from rich import print
from rich.panel import Panel

def main():
    t = Termostato()
    t.temperatura = 26.5
    msg = Panel(f'A temperatura esta em {t.ftemperatura()}', title='Termostato', width=33)
    print(msg)


if __name__ == '__main__':
    main()