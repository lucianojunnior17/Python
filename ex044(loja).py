print('\033[31m=\033[m'*261)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*261)
preco = float(input('Preço da Compra: R$: '))
print('''Forma de Paggamento
[1] à vista dimheiro /Cheque
[2] à vista no cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão ''')
opcao = int((input('Qual é a opção? ')))

if opcao ==1:
    total = preco - (preco * 10 /100)
elif opcao ==2:
    total = preco - (preco * 5 /100)
elif opcao ==3:
    total = preco
    parcela = preco / 2
    print('Sua Compra será parcelada em 2x de R$ {:.2f} SEM JUROS '.format(parcela))
elif opcao ==4:
    total = preco + (preco * 20 /100)
    totaparc = int(input('Quantas Parcelas ? '))
    parcela = total / totaparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS '.format(totaparc,total))
else:
    total = 0
    print('OPÇÂO INVÀLIDA DE PAGAMNETO')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final. '.format(preco,total))

