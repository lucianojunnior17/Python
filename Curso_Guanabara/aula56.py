somaidade = 0
mediaidade = 0
maioridadehomenm = 0
nomevelho = ''
totmulher20 = 0 
for p in range(1,5):
    print('-----{} PESSOA ------'.format(p))
    nome = str(input('Digite o nome da Pessoa :')).strip()
    idade = int(input('Digite a Idade da Pessoa: '))
    sexo = str(input('Digite o Sexo [M/F]')).strip()
    somaidade +=  idade
    if p == 1 and sexo in 'm':
        maioridadehomenm = idade
        nomevelho = nome
    if sexo in 'm' and idade > maioridadehomenm:
        maioridadehomenm = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher20 +=1
mediaidade = somaidade / 4 
print('A média de idade do grupo é de {} anos '.format(mediaidade))
print('O homen mais velho tem {} anos e se chama {}'.format(maioridadehomenm,nomevelho))
print('Ao todo são {} mulheres com  menos de 20 anos'.format(totmulher20))