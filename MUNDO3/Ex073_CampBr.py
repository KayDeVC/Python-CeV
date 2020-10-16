camp = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
        'Vasco da Gama', 'Chapecoense', 'Atlético MG', 'Botafogo', 'Atlético PR',
        'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
        'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético GO')
print('\n')
print('-'*40)
print(f'Lista de times do Brasileirão: {camp}')
print('-'*40)
print(f'Os 5 primeiros são: {camp[:5]}')
print('-'*40)
print(f'Os 4 últimos são: {camp[-4:]}')
print('-'*40)
print(f'Em ordem alfabética: {sorted(camp)}')
print('-'*40)
print(f'O Chapecoense está na {camp.index("Chapecoense")+1}a posição.')