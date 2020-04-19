##Gerador de PA###
print('='*157)
print('Vamos calcular a Progressão aritimética de um número e mostras os 10 primeiros resultagos')
primeiro = int(input('Digite o Primeiro núimero : '))
razão = int(input('Digite a razão da PA '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} = '.format(termo), end='')
    termo += razão
    contador += 1
print('='*157)
print('FIM')
