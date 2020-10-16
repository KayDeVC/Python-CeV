print('\n{:=^40}'.format(' PROGRESSÃO ARITMÉTICA - PA '))
p1 = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
a = p1
print(p1, end = ' -> ')
for c in range(0, 9):
    a += rz
    print(a, end =' -> ')
print('ACABOU')