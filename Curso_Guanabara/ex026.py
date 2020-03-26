frase = str(input('Digite Uma frase : ')).upper().strip()
print(' A Letra A aparede {} vezes na frase .'.format(frase.count('A')))
print(' A primeira letra A  apareec na posição {}'.format(frase.find('A')+1))
print(' A ultima letra A apareceu {} '.format(frase.rfind('A')+1))


