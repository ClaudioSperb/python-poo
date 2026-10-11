from rich import print

class Avaliacao:
    def __init__(self, nome, disciplina, nota= 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # ATRIBUTO PROTEGIDO ( # ) - protected

    #METODOS ACESSORES
    def get_nota(self): #Método Getter - PEGAR NOTA
        return self._nota

    def set_nota(self, valor): #Método Setter - Valida a nota
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print(f'[red b]NOTA INVÁLIDA[/]')