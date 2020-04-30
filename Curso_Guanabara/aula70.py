#####EXERCÍCIOS 70 #######
print('-'*50)
print('{^} LOJA DO BARATÃO')
print('-'*50)
menor = cont = caro = total = 0
barato = 'a'
while True:
    produto = str(input('DIGITE O NOME DO PRODUTO : '))
    cont += 1 
    preço = float(input('Digite o valor do produto : '))
    total += preço
    if preço >=1000:
        caro += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
   
    resp = '1'
    while resp not in "SN":
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*50)
print(f'{caro} Produtos estão acima de 1000 R$ ')
print(f'O total da compra foi de {total:10.2f}')
print(f'O produto mais barato é {barato}  e custou {menor:10.2f}')
print('FIM DO PROGRAMA')