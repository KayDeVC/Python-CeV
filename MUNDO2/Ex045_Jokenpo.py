from time import sleep
from random import randint
print('\n\33[1;32m{:+^40}\33[m'.format(' JOKENPÔ '))
print('\nVamos jogar?')
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jog = int(input('Qual a sua jogada? '))
print('\n  JO')
sleep(1)
print('     KEN')
sleep(1)
print('         PÔ\n')
print('-='*20)
print('Computador jogou: {}'.format(itens[comp]))
print('Jogador jogou: {}'.format(itens[jog]))
print('-='*20)
if comp == 0: # Computador jogou Pedra
    if jog == 0:
        print('\n\33[1;33mEMPATE!\33[m')
    elif jog == 1:
        print('\n\33[1;32mJOGADOR VENCEU\33[m!')
    elif jog == 2:
        print('\n\33[1;31mCOMPUTADOR VENCEU\33[m!')
    else:
        print('\n\33[32;43mJOGADA INVÁLIDA!!\33[m')
elif comp == 1: # Comoutador jogou Papel
    if jog == 0:
        print('\n\33[1;31mCOMPUTADOR VENCEU\33[m!')
    elif jog == 1:
        print('\n\33[1;33mEMPATE!\33[m')
    elif jog == 2:
        print('\n\33[1;32mJOGADOR VENCEU\33[m!')
    else:
        print('\n\33[32;43mJOGADA INVÁLIDA!!\33[m')
elif comp == 2: # Computador jogou Tesoura
    if jog == 0:
        print('\n\33[1;32mJOGADOR VENCEU\33[m!')
    elif jog == 1:
        print('\n\33[1;31mCOMPUTADOR VENCEU\33[m!')
    elif jog == 2:
        print('\n\33[1;33mEMPATE!\33[m')
    else:
        print('\n\33[32;43mJOGADA INVÁLIDA!!\33[m')
