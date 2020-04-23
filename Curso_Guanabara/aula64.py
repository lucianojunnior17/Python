####Aula 64 Curso em Vídeo######
n = cont = soma = 0 
n = int(input('Digite um número : '))

while n != 999:    
    soma += n
    cont += 1
    n = int(input('Digite um número : '))
print('você digitou {} números e a soma foi {} '.format(cont,soma))

