class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    #METODOS ACESSORES
    def get_nota(self): #Método Getter - PEGAR NOTA
        return self._nota

    def set_nota(self): #Método Setter - Valida a nota
        pass