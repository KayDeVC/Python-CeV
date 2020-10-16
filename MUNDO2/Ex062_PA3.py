print('\n\33[32m{:=^40}\33[m'.format(' PROGRESSÃO ARITMÉTICA - PA '))
p1 = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end = ' -> ')
        termo += rz
        cont += 1
    print('PAUSA')
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print('\n\33[33mProgressão realizada com {} termos.'.format(total))
print('\n\33[1;31mFIM DO PROGRAMA\33[m')