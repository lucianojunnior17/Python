from datetime import date
atual = date.today().year
print('Esse é o programa do exército Basileiro !!!!')
nasc = int(input('Digite o ano que você nasceu : '))
sex = str(input('Qual seu Sexo [F] ou [M]: '))
idade = atual - nasc
print('Quem naceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if sex == 'f':
    print('\33[35m Somente homens são permitios no exército')
elif idade == 18 and sex == 'm':
    print('\33[32m você deve se alista imediatamente !!!!!!!')
elif idade < 18 and sex == 'm':
    saldo = (18 - idade)
    print('\33[33m Você ainda não tem idade para o alistamento. Faltan {} anos '.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = (idade - 18)
    print('\33[31m Voce já deveria ter se alistado há {} anos '.format(saldo))
    ano = atual - saldo
    print('Você deveria ter se alistado em {}'.format(ano))

