from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


a1 = Aluno('Claudio', 36, 'ADS', 'T01')
a1.fazer_aniversário()
a1.fazer_matricula()
#inspect(a1, methods=True)

p1 = Professor('Gustavo Guanabara', 45, 'T.I', 'Mestrado')
p1.fazer_aniversário()
p1.dar_aula()
#inspect(p1, methods=True)

f1 = Funcionario('Claudio', 36, 'Gerente', 'Comercial')
f1.fazer_aniversário()
f1.bater_pontos()
#inspect(f1, methods=True)