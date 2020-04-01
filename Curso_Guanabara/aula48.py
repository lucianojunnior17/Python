#Soma dos números impares multiplo de tres
soma = 0
conta = 0
for cont in range (1,501,2):
    if cont % 3 == 0:
        conta = conta +1
        print(cont, end=' ')
        soma = soma + cont 
print('foram {} valores somados'.format(conta))
print('A soma de todos os valores solicitados é {}'.format(soma))
