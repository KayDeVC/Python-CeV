print('\n{:=^40}'.format(' NÚMERO PRIMO? '))
num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        tot += 1
        print('\33[33m', end = ' ')
    else:
        print('\33[31m', end = ' ')
    print(c, end = '')
print('\n\33[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Portanto ele é um número PRIMO!')
else:
    print('Portanto ele NÃO é um número primo')