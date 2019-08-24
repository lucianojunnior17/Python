num = int(input('Escolha um número inteiro : '))
print(''' Escolha uma das bases para a conversão : 
[1] Converter para binário (base 2 ) 
[2] Converter para Octal (base 8 ) 
[3] Converte para hexadecimal''')
opcao = int(input('Sua opção : '))
if opcao == 1:
    print('{} Convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertedo para Octal é igual a {} '.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual a {} '.format(num, hex(num)[2:]))
else:
    print('Opção Inválida')

