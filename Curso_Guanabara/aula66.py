##### Exercício 66 #####
###### Exercício 66 Python curso em video ######
cont = soma  = 0
while True:
    num = int(input('Digite um número : [999 para parar]'))
    if num == 999:
        break
    cont += 1 
    soma += num
print(f'A soma dos {cont} valores foi de {soma}')
print('Acabou')