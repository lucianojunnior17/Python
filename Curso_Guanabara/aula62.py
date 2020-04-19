##Gerador de PA###
print('='*157)
print('Vamos calcular a Progressão aritimética de um número e mostras os 10 primeiros resultagos')
primeiro = int(input('Digite o Primeiro núimero : '))
razão = int(input('Digite a razão da PA '))
termo = primeiro
contador = 1
total = 0
mais = 0 
while mais != 0:
    total = total + mais
    while contador <= total:
        print('='*157)
        print('{} = '.format(termo), end='')
        termo += razão
        contador += 1
        print('='*157)
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar mais ?;  '))
print('FIM')
