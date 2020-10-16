print('\n{:=^40}'.format(' PROGRESSÃO ARITMÉTICA - PA '))
p1 = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
termo = p1
cont = 1
while cont <= 10:
    print(termo, end =' -> ')
    termo += rz
    cont += 1
print('ACABOU')