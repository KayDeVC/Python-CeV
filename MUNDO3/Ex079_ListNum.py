lista = []
while True:
    n  = int(input('\nDigite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicioná-lo!')
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
print('*'*40)
print(f'\nVocê digitou os valores {sorted(lista)}.')
print('\nFIM DO PROGRAMA')