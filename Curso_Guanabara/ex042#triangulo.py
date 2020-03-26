print('\033[31m=\033[m'*261)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*261)
r1 = float(input('Primeiro Segmento : '))
r2 = float(input('Segundo Segemento : '))
r3 = float(input('Terceiro Segmento : '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os segmentos \033[35mPodem Formar um Triângulo!!!\033[m', end='  ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
            print('ESCALENO')
    else:
        print('ISÓSELES')
else:
    print('Os segmentos \033[31mNÃO PODEM \033[mformar um Triângulo ....')
