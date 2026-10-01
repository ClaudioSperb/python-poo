from funcionario import Gerente, Programador
from rich import print

def main():
    gerente = Gerente('Claudio Sperb', 2000, 15)
    gerente.bonus()
    gerente.mostrar_dados()

    programador = Programador('Claudio Sperb', 5000, 10, 'Python')
    programador.mostrar_dados()

if __name__ == '__main__':
    main()