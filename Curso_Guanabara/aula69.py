print('-'*50)
print('Programa de cadastro de pessoas ')
print(''*50)
tot18 = 0 
toth =0
totm20 =  0
while True:
    nome = str(input('Digite um nome : '))
    idade = int(input('Informe a idade da pessoa : '))
    sexo = 'a'
    while sexo not in "FM":
        sexo = str(input(' Sexo [M/F] ')).strip().upper()[0]
    if idade >=18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'M' and idade < 20 :
        totm20+= 1    
    resp = 'a'
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == "N":
        break
print(f'O total de pessoas maiores de 18 é  {tot18}')
print(f'Ao todo temos {toth} homens cadastrado')
print(f'E temos {totm20} Mulheres com menos de 20 anos ' )
print('Acabou')


