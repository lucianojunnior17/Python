from time import sleep
print(' Olá programa feito para brinar om números ')
sleep(3)
n1 = int(input('Primeiro valor'))
n2 = int(input('Segundo valor'))
opção = 0
while opção != 5:
    print('''[1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA ''')
    opção = int(input('Qual é a sua opção ? '))

    if opção == 1:
        soma = n1+n2
        print('A soma de {} e {} é {}'.format(n1,n2,soma))
        sleep(3)
          
    elif opção == 2 :
        multi= n1*n2
        print('A Multipliacçao de {} e {} é {} '.format(n1,n2,multi))
        sleep(3)
    elif opção == 3:
        if n1 > n2 : 
            maoir = n1
        else:
            maoir = n2
        print('O maoir número entre {} e {} é {} '.format(n1,n2,maoir))
        sleep(3)
    elif opção == 4 :
        print('Informe os novos números')
        n1 = int(input('Insira o primeiro valor'))
        n2 = int(input('Insira o segundo valor'))
    elif opção == 5 :        
        print('Saindo do Programa')
        sleep(2)       
print('Fim do Programa!!!')
