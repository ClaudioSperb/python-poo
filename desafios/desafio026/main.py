from funcionarios import *
from rich import print, inspect

def main():
    f1 = FuncionarioMensalista('Claudio Sperb', 8500)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = FuncionarioHorista('Josiane Segatto', 25, 250)
    f2.calcular_salario()
    f2.analisar_salario()

if __name__ == '__main__':
    main()