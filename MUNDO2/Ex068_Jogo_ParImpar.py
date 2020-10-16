from random import randint
print('\n\33[1;34m', end = '')
print('=-'* 20)
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR?'))
print('=-'* 20)
print('\33[m')
cont = 0
while True:
    maq = randint(0,10)
    num = int(input('\nDiga um número de 0 a 10: '))
    paim = str(input('Par ou ímpar? [P/I] ')).strip()[0]
    res = num + maq
    if paim in 'Pp' and res % 2 == 0:
        print(f'\n\33[32mVocê jogou {num} e o computador jogou {maq}\n{res} é PAR e você venceu!\33[m')
        cont += 1
    elif paim in 'Pp' and res % 2 != 0:
        print(f'\n\33[31mVocê jogou {num} e o computador jogou {maq}\n{res} é ÍMPAR e você perdeu!\33[m')
        break
    elif paim in 'Ii' and res % 2 != 0:
        print(f'\n\33[32mVocê jogou {num} e o computador jogou {maq}\n{res} é ÍMPAR e você venceu!\33[m')
        cont += 1
    elif paim in 'Ii' and res % 2 == 0:
        print(f'\n\33[31mVocê jogou {num} e o computador jogou {maq}\n{res} é PAR e você perdeu!\33[m')
        break
    else:
        print('\nAção inválida. Recomeçando...')
print(f'\n\33[33mGAME OVER! Você venceu {cont} vezes.\33[m')