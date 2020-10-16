lista1 = []
lista2 = []
lista3 = []
print()
print(f'{" 3 LISTAS ":=^40}')
while True:
    l1 = int(input('\nDigite um valor: '))
    lista1.append(l1)
    if l1 % 2 == 0:
        lista2.append(l1)
    elif l1 % 2 == 1:
        lista3.append(l1)
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
print()
print('-='*21)
print(f'\nA lista completa de valores é:\n{lista1}')
print(f'\nA lista somente com pares é:\n{lista2}')
print(f'\nE a lista somente com ímpares é:\n{lista3}')