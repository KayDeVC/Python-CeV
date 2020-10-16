print('\n', end = '')
print('{:=^40}'.format(' MERCADO PEIXOTO '))
total = mmil = menor = cont = 0
barato = ''
while True:
    print('\n', end = '')
    print('*'*40)
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    print('*'*40)
    cont += 1
    total += preço
    if preço > 1000:
        mmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    esc = ' '
    while esc not in 'SN':
       esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
print('\n', end = '')
print('{:-^40}'.format(' FIM DAS COMPRAS '))
print(f'\nO total gasto foi de R${total:.2f}!')
print(f'{mmil} produtos custaram mais de R$1000,00!')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}!')