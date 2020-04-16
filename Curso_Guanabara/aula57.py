sexo = str(input('Informe seu sexo : ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos Por favor digite novamente : ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

