print('\033[31m=\033[m'*300)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*300)
print('Olá esse programa vai ajudar voçê a calcular a sua nota nas Provas')
materia = (input('Digite o Nome da Matéria : ')).capitalize()
pesotrab = str(input('Sua Matéria tem algum trabalho que vale nota ? [S] ou [N] : ')).upper()
peso1 = float(input('Digite o peso da P1 : '))
peso2 = float(input('Digite O peso da P2 : '))
pesoprev = float(input('Digite o peso as prévias :'))

if pesotrab =='S':
    notatrab = float(input('Digite o peso do Trabalho : '))
    media2 = (nota1 * (peso1 / 100)) + (nota2 * (peso2 / 100)) + (previa * (pesoprev / 100) + notatrab * (pesotrab / 100))
else:

nota1 = float(input('Digite a nota da P1 : '))
nota2 = float(input('Digite a nota da P2 : '))
previa = float(input('Digite a nota de prévia : '))
media = (nota1 * (peso1 / 100)) + (nota2 * (peso2 / 100)) + (previa * (pesoprev / 100))
print(' A média do aluno em {} é  {:.1f} '.format(materia, media))
if media >= 7:
    print('Aprovado ')
else:
    print('Reprovado')
