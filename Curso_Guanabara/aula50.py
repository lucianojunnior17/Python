##Exercícios 50 Curso em vídeo Gustavo Guanabara##
soma = 0
cont = 0
for n in range (1,7):
    num= int(input('Digite um {} Valor : '.format(n)))
    if num % 2 ==0:
        soma = soma+num
        cont = cont + 1
print('Voçê informou {} números e a soma deles é {}'.format(cont,soma))