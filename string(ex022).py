nome = str(input('Digite seu nome completo : ')).strip()
print('Analizando seu nome ...')
print('Seu nome em letras miúsculas é {}'.format(nome.upper()))
print('Seu nome em letra minúclas é {}'.format(nome.lower()))
print('Seu nome contem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))
