casa = float(input('Qual é o valor da casa  R$ ? '))
salario = float(input('Qual é o seu salário R$ ? '))
ano = int(input('em quantos anos deseja pagar  ? '))
prestacao = casa / (ano * 12)
minimo = salario * 0.30
if prestacao <= minimo:
    print('\033[34O emprestímo foi aceito\033[m')
else:
    print('\033[31mO EMPRESTIMO NÃO FOI APROVADO !!!!\033[m')
print('para pagar uma casa de R$ {:.2f} em {} anos a prestação será de {:.2f} R$ '.format(casa, ano, prestacao))
