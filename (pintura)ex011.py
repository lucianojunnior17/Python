largura = float(input('Qual a Largura da Parede ? :'))
altura = float(input(' Qual a Altura da Parede ? : '))
area = largura * altura
print('Sua Parede tem {} de Largura por {} de Altura. A Área é de {:.2f}m² '.format(largura, altura, area))
tinta = area / 2
print('Para Pintar essa parede é necessário {} de tinta. '.format(tinta))

