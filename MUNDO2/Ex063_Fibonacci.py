print('\n')
print('-' * 40)
print(' Sequência FIBONACCI ')
print('-' * 40)
qtd = int(input('Quantos termos você quer mostrar? '))
cont = 3
t1 = 0
t2 = 1
print('~' * 40)
print('{} → {} → '.format(t1, t2), end = '')
while cont <= qtd:
    t3 = t1 + t2
    print(t3, end = ' → ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~' * 40)