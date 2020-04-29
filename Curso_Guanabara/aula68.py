from random import randint
print('-'*50)
print('Vamos Jogar PAR ou IMPAR ')
print('-'*50)

v = 0

while True:
    jogador = int(input('Digite um valor : '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ''   
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2:
            print('Você venceu !!')
            v += 1 
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("Você venceu")
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente')    
print('Game Over')


