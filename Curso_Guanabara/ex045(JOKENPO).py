from time import sleep

print('\033[31m=\033[m'*261)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*261)
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print( 'O computador Escolheu {}'.format(itens[computador]))
print(''''Suas opçôes São: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é  a sua jogada ? : '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!!')
print('\033[31m=\033[m'*261)
print('\033[31m=\033[m'*261)
print('Computador Escolheu {}'.format(itens[computador]))
print('O Jogador Escolheu {}'.format(itens[jogador]))
if  computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('\033[33mEmpatou!!!')
    elif jogador == 1:
        print('\033[34mJogador Venceu!!!')
    elif jogador == 2:
        print('\033[31mComputador venceu!!!')
    else:
        print('\033[31mJOGADA INVÁLIDA!!!')
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('\033[34mJogador Venceu')
    elif jogador == 1:
        print('\033[33mEmpatou')
    elif jogador == 2:
        print('\033[31mComputador Venceu')
    else:
        print('\033[31mJOGADA INVÁLIDA!!!')

elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('\033[34mJogador Venceu')
    elif jogador == 1:
        print('\033[31mComputador venceu')
    elif jogador == 2:
        print('\033[33mEmpatou')
    else:
        print('\033[31mJOGADA INVÁLIDA!!!')

