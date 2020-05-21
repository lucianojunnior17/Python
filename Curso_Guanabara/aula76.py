#########Exercício 76 Curso de Python###########
produtos = ('Lapis',1.75,
            'Borracha',2.00,
            'Caderno',15.90,
            'Estojo',25,
            'Trasferidor',12.85,
            'Mangá',14.90,
            'Mochila',69.90,
            'Caneta',1.50)
print('='*40)
print(f'{"Listagem de Preços":^40}')
print('='*40)
###print(produtos)
for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else:
        print(f'R${produtos[pos]:>5.2f}')
print('='*40)