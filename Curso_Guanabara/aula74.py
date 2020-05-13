from random import randint
numeros = randint(1,10), randint(1,10),randint(1,10),randint(1,10),randint(1,10)
for n in numeros:
    print(f'{n}')
print(f' O maior valor sorteado foi : {max(numeros)}')
print(f'O menor valor sorteado foi : {min(numeros)}')