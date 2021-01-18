###################EXERCICIO 81 ########################
########### CURSO DE PYTOHN MUNDO 3 ####################
########### PROF. GUANABARA ############################
valores = []

while True:
    valores.append(int(input('Digite um valor : ')))
    res = str(input('Quer Continuar ? [S/N] : '))
    if res in 'Nn':
        break
print('='*130)
print(f'Você digitou {len(valores)} elementos ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores} ')
if 5 in valores: 
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')