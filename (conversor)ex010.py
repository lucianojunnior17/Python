real = float(input('Quanto você tem na carteira ? R$:  '))
dolar = real / 3.843
libras = real / 5.130
euro = real / 4.540
yenes = real / 0.035
franco = real / 3.9000
austdollar = real / 2.870
candollar = real / 1.310

print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))
print('Ou {:.2f} Libras \n {:.2f} Euros \n {:.2f} Yenes \n {:.2f} Francos Franceses \n {:.2f}Dollar Canadense \n {:.2f} Dollar Australiano.'.format(libras, euro, yenes, franco, candollar ,austdollar))
