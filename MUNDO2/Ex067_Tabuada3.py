print('\n{:=^30}'.format(' TABUADA '))
while True:
    num = int(input('\nQual o número desejado: '))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num:2} x {cont:2} = {num * cont:2}')
    print('\n', end = '')
    print('='*30)
print('\n\33[1;31mFIM DO PROGRAMA TABUADA\n\33[m')
print('='*30)