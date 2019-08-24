a = int(input('Digite o primeiro número : '))
b = int(input('Digite o Segundo número : '))
c = int(input("Digite o terceiro Número : "))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
        menor = c
print('O menor valor é {}'.format(menor))
