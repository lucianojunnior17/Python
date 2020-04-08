###Aula 52 Curso em vídeo Gustavo Guanabara
###### Saber se o número é primo
print('='*200)
print("Luciano Lima jr.")
print('='*200)
num = int(input(' Digite um Nímero : '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('Divisivel')
        tot += 1
    else:
            print('Não divisivel')
            print('{}'.format(c), end=' ')
if tot == 2:
    print('='*200)
    print('O Número {} é primo '.format(num))
else:
        print('='*200)
        print('O Número {} não é primo '.format(num))
print('**FIM**')

   