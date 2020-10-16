prod = ('Laptop', 1500, 'CPU', 2450, 'Mouse', 43.9, 'Headphone', 875, 'Mousepad', 55.9)
print('\n', end = '')
print('-='*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-='*20)
for pos in range(0, len(prod)):
    if pos % 2 == 0:
        print(f'{prod[pos]:.<30}', end = '')
    else:
        print(f'R${prod[pos]:>7.2f}')
print('-='*20)