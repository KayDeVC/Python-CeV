from time import sleep
print('\n')
print('=-+'*14)
print('\n\33[33m{:=^40}\33[m'.format(' MENU 2 NÚMEROS '))
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    print('''
[ 1 ] Soma dos valores
[ 2 ] Multiplicação dos valores
[ 3 ] Descobrir qual deles é maior
[ 4 ] Novos valores
[ 5 ] Sair do Programa''')
    opc = int(input('Qual a sua opção?: '))
    if opc == 1:
        print('\n\33[35mA soma de {} e {} é: {}.\33[m'.format(num1, num2, num1 + num2))
    elif opc == 2:
        print('\n\33[36mO produto de {} e {} é: {}.\33[m'.format(num1, num2, num1 * num2))
    elif opc == 3:
        if num1 > num2:
            print('\n\33[32mEntre {} e {} o maior valor é {}.\33[m'.format(num1, num2, num1)) 
        elif num2 > num1:
            print('\n\33[32mEntre {} e {} o maior valor é {}.\33[m'.format(num1, num2, num2)) 
        else:
            print('\n\33[32mOs dois valores são iguais.\33[m')
    elif opc == 4:
        print('\n\33[34mInforme novos valores\33[m')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('\nFinalizando...')
        sleep(1.5)
    else:
        print('\n\33[1;33mCOMANDO INVÁLIDO\33[m')
print('\n\33[1;31mFIM DO PROGRAMA\33[m')