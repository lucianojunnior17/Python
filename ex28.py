from random import randint
print('='*200)
print('='*200)
print('Vou pensar em um número de 0 a 5 ')
pc = randint(0, 5)
jogador = int(input('Escolha um número de 0 a 5 !! : '))

if jogador == pc:
    print('Parabéns você venceu')
else:print('Voce perdeu')
