print('\033[31m=\033[m'*300)
print('\033[30m PROGRAMA DE LUCIANO JUNIOR\033[m')
print('\033[31m=\033[m'*300)
print('\033[31m PROGRAMA PARA TOMAR VERGONHA NA CARA\033[m')
salario = float(input('Quanto você ganha? : '))
poupa = salario * 0.30
viva = salario * 0.70
nece = poupa * 0.55
educa = viva * 0.05
zona = viva * 0.10
if salario > 952.00:
    print(' Você tem para gastar esse mês \033[7;30;44m{:.2f}\033[m'.format(viva))
    print('Desses {:.2f} você deve gastar \033[1;30;41m{:.2f}\033[m em coisas necessárias'.format(viva, nece))
    print('Você deve economizar {:.2f}'.format(poupa))
    print('Para educação você tem para gastar {:.2f}'.format(educa))
    print('Você tem {:.2f} para gastar a vontade'.format(zona))

else:
    print('Esse programa não foi feito para você !!!!!!!!!!!!!!!!')
print('\033[31m=\033[m'*300)
