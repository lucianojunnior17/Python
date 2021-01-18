#################EXERCICIO 81 ########################
########### CURSO DE PYTOHN MUNDO 3 ####################
########### PROF. GUANABARA ############################


valores = []
vpares = []
vimpares = []
while True:
    valores.append(int(input('Digite um Número : ')))
    res = str(input('Quer Continuar ? [S/N] : '))
    if res in 'Nn':
        break
print('='*75)
print(f'Os valores foram {valores}')
print(f'Você digitou {len(valores)}) elementos')
if valores % 2 == 0:
    vpares.append(vpares)
    print(f'Is valores pares são {vpares}')
elif valores % 2 == 1:
    vimpares.append(vimpares)
    print(f' Os valores Impares são {vimpares}')
