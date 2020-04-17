###Programa Calcular O Fatorial dos Números###
print('Programa para calcular o fatorial')
n = int(input('Digite um números : '))
c = n 
f = 1
print(' Calculando  !{} '.format(n))
while c > 0: 
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(' {} '.format(f))
