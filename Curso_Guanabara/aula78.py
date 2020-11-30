#########Exercício 78 Curso de Python###########
################################################
###############MAIOR E MENOR VALORES DA LISTA###

listaum = []
mai = 0
men = 0
for c in range(0,5):
    listaum.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        mai= men =listaum[c]
    else:
        if listaum[c] > mai:
            mai = listaum[c]
        if  listaum[c] < men:
            men = listaum[c]

print('=== '*30)
print(f' Você digitou os valores {listaum}')
print(f'O maior valor digitado foi {mai} na posição ', end='')
for i, v in enumerate(listaum):
    if v == mai:
        print(f'{i}.....')
print()
print(f'O menor valor digitado foi {men} na posição ', end='')
for i, v in enumerate(listgit   aum):
    if v == men:
        print(f'{i}.....')
