from math import factorial #Módulo direto

print('\n ===> CALCULANDO FATORIAIS <===')
num = int(input ('Digite um n° pra calcular seu fatorial: '))
cont = num
fat = 1
print('\nCalculando o fatorial de {}!'.format(num))
while cont > 0:
    print('{}'.format(cont), end = '')
    print(' x ' if cont > 1 else ' = ', end = '')
    fat *= cont
    cont -= 1
print('{}'.format(fat))

f = factorial(num) #Modo fácil
print('\n',f)