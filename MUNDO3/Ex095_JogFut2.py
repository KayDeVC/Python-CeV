time = []
jogador = {}
gols = []
print()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} participou: '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f' Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        esc = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if esc in 'SN':
            break
        print('ERRO. Digite apenas "S" ou "N".')
    if esc == 'N':
        break  
print('-='*21)
print('cod ', end = '')
for i in jogador.keys():
    print(f'{i:^14}', end = '')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:<3}', end = '')
    for d in v.values():
        print(f'{str(d):^14}', end = '')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 pára) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO. Não existe jogador com o código {busca}.')
    else:
        print(f'  -- Levantando dados do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  -> Na partida {i+1} ele marcou {g} gols.')
        print('-'*40)
print(' <<< ✓✓ VOLTE SEMPRE ✓✓ >>>')