print('\033[31m=\033[m'*261)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*261)
disp = float(input('Quanto você tem no mês  ? : '))
seg = float(input('Quantas Segundas Feiras tem no mês ? : '))
pas = float(input('Quantas Passagens irá gastar ? '))
cel = str(input('Irá colocar crédiotos no celular ? [S] ou [N] : ')).upper()
ing = str(input('Vai ao cinema esse mês ? [S] ou [N] :  ')).upper()
lan = float(input('Quantos lanches vai comer ? : '))

print('\033[31m=\033[m'*261)

lann = lan * 10.50
folga = seg * 19.90
bus = pas * 5.05
total = lann + folga + bus
totalr = disp - total

if cel == 'S':
    cell =39.90
    print('Em Créditos no celular {:.2f}'.format(cell))
    total = cell + total

else:
    print('\033[35mVocê não vai colocar créditos esse mês\033[m ')

if ing == 'S':
    ingg =12.50
    print('irá gastar {:.2f}R$ no Cinema : '.format(ingg))
    total = ingg + total
else:
    print('\033[35[mvocê não irá ao cinema\033[m ')

print('Você irá gastar {:.2f} R$  em Comidas Esse Mês '.format(folga))
print('Irá gastar {:.2f} em Passagens '.format(bus))
print('Irá gatar de lanches {:.2f}'.format(lann))
print('Irá ter um \033[31mgasto Total de {:.2f}\033[m no Mês '.format(total))
print('Resta {:.2f}'.format(totalr))



