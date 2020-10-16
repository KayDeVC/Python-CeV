pessoas = list()
aux = list()
pes = lev = 0
while True:
    aux.append(str(input('\nNome: ')))
    aux.append(float(input('Peso (Kg): ')))
    if len(pessoas) == 0:
        pes = lev = aux[1]
    else:
        if aux[1] > pes:
            pes = aux[1]
        if aux[1] < lev:
            lev = aux[1]
    pessoas.append(aux[:])
    aux.clear()
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
print('*'*40)   
print(f'\nAo todo foram cadastradas {len(pessoas)} pessoas.')
print(f'\nO maior peso apresentado foi {pes}kg.\nPeso de ', end = '')
for p in pessoas:
    if p[1] == pes:
        print(f'[{p[0]}] ',end = '')
print(f'\n\nO menor peso apresentado foi {lev}kg.\nPeso de ', end = '')
for p in pessoas:
    if p[1] == lev:
        print(f'[{p[0]}] ', end = '')
print()