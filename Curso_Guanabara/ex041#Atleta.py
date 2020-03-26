print('\033[31m=\033[m'*261)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*261)
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento : '))
idade = atual - nascimento
print('O Atleta tem {} anos '.format(idade))
if idade <= 9:
    print('Classificação : MIRIM ')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação : JUNÍOR')
elif idade <= 25:
    print('Classificação : SÊNIOR')
else:
    print('Classificação : MASTERS')
