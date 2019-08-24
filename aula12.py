nome = str(input('Qual é o seu nome ? : '))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Maria' or nome ==  'Pedro' or nome == 'João':
    print('Seu nome é bem popular ^^ ')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Lindo nome de Menina *-* : {}'.format(nome))
else:
    print('Seu nome é muito normal')
print('tenha um ótimo dia : {} '.format(nome))

