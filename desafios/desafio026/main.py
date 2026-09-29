from funcionarios import *
from rich import print, inspect

def main():
    f1 = FuncionarioHorista('Claudio Sperb', 12, 190)
    inspect(f1)

if __name__ == '__main__':
    main()