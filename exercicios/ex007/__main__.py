from classes import Professor, Aluno, Funcionario
from rich import print,inspect

def main():
    a1 = Aluno('Claudio', 36, 'ADS', 'T01')
    a1.fazer_aniversário()
    a1.fazer_matricula()
    a1.estudar()
    #inspect(a1, methods=True)

    p1 = Professor('Gustavo Guanabara', 45, 'T.I', 'Mestrado')
    p1.fazer_aniversário()
    p1.dar_aula()
    p1.estudar()
    #inspect(p1, methods=True)

    f1 = Funcionario('Claudio', 36, 'Gerente', 'Comercial')
    f1.fazer_aniversário()
    f1.bater_pontos()
    f1.estudar()
    #inspect(f1, methods=True)

if __name__ == '__main__':
    main()