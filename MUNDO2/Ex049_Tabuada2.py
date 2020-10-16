num = int(input('\nQual o número desejado: '))
print('{:=^30}'.format(' TABOADA '))
for c in range(0, 11):
    tab = num * c
    print('{:2} x {:2} = {:2}'.format(num, c, tab))
print('='*30)