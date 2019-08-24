velocidade = float(input('Qual é a velocidade do Carro? : '))
if velocidade > 80:
    print('Você foi multado!!!! , Exedeu o limite de velocidade que é de 80Km/h')
    multa = (velocidade - 80)*7
    print('Voce dve pagar uma multa no valor de {:.2f}'.format(multa))

print('Tenha um Bom dia!!!!')
