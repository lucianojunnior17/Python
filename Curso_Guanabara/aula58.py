from random import randint
pc = randint(0, 10)
print('='*200)
print('='*200)
print('Olá sou seu computador vamos jogar?? ')
print('Vou pensar em um número de 0 a 10 ')
print('Tente acertar qual número eu escolhi ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ? '))
    palpites += 1
    if jogador == pc:
        acertou = True
        print('Parabéns você acertou !!!!!')
    else:
        if jogador < pc:
            print('Mais...')
            print('Tente outra vez')
        if jogador > pc:
            print('Menor')
            print('Tente outr vez')
print('Você acertou com {} tentativas '.format(palpites))
