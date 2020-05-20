numero = (int(input('Digite o Primeiro Número : ')),
      int(input('Digite o segundo  Número : ')),
      int(input('Digite terceiro  Número : ')),
      int(input('Digite o ultimo Número : ')))
print(f'Você digitou os seguintes números {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes ')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1} posição ')
else:
    print('O valor 3 não foi digitado')
print('Os valores digitados foram ')

for n in numero:
    if numero % 2 == 0 :
        print(n, end=' ')
