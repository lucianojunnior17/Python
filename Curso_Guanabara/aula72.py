cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
        'nove','10','onze','doze','treze','quatorze','quize', 'dezeseis',
        'dezessete','dezoito','dezenove','vinte','vinte um ','vinte dois',
        'vinte três','vinte Quatro','vinte Cinco')
while True:
    num = int(input('Digite um número entre 0 e 25 : '))
    if 0 <= num <= 25:
        break
    else:
        num = cont
    print('Tente novamente : ', end='')
print(f'Você digitou o número {cont[num]}')