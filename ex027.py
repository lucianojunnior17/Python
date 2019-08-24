n = str(input('Digite seu nome Completo : ')).strip().upper()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu Ultimo nome é {} '.format(nome[len(nome) - 1]))