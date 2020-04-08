###Aula 53 Curso em vídeo Gustavo Guanabara
###### PALINDROMO
print('='*200)
print("Luciano Lima jr.")
print('='*200)
frase = str(input('Digite uma frase : ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1 , -1):
    inverso += junto[letra]
if inverso == junto:
    print('é uma PALINDROMO')
else:
    print('Não é palindromo')

