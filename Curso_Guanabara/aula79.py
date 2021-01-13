###################EXERCICIO 79 ########################
########### CURSO DE PYTOHN MUNDO 3 ####################
########### PROF. GUANABARA ############################

numero = list()
while True:
    n = int(input('Digite um valor : '))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado com sucesso !!!')
    else:
        print('Valor Duplicado não adicionado : ')
    r = str(input('Quer continuar ? '))
    if r in 'Nn':
        break

print('=='*30)
numero.sort()
print(f'Você digitou os valores {numero}')
print('=='*30)