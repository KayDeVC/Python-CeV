print('\n', end = '')
print('='*40)
print('{:^40}'.format('BANCO CITY'))
print('='*40)
valor = int(input('\nQue valor você deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('\n', end = '')
print('='*40)
print('\nVolte sempre ao Banco City. Tenha um ótimo dia!')