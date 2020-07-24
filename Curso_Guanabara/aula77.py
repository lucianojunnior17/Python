#########Exercício 77 Curso de Python##########
##########CONTADOR DE VOGAIS##############################
palavras = ('Aprender ', 'programar', 'Computacao', 'Python','curso',
'gratis', 'engenheiro', 'programador')

for p in palavras:
    print(f'\n na palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')