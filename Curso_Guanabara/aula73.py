#######Exercício 73 Curso de Python Gustvo Guanabara######
#######Tabela Campeonato Brasileiro#######
print('='*100)
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruziero', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo','Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 
         'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
for t in times:
    print(t)
print('='*100)
print(f'Os 5 primeiros times são : {times[0:5]}')
print('='*100)
print(f'Os quatros ultimos são : {times[-4:]}')
print('='*100)
print(f'Times em ordem alfabética : {sorted(times)}')
print('='*100)
print(f'O time da Chapecoense está na {times.index("Chapecoense")+1} posição ')
print('='*100)
