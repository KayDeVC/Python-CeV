import random
print('\n{:=^40}'.format(' Humano vs máquina '))
print('Estou pensando em um número de 0 a 10!')
cont = 1
num = random.randint(0,10)
meu = int(input('Qual número estou pensando? '))
while meu != num:
    cont += 1
    if meu > num:
        print('\33[31mMenos...\33[m', end = '')
        meu = int(input('Tente de novo: '))
    elif meu < num:
        print('\33[33mMais...\33[m', end = '')
        meu = int(input('Tente de novo: '))
if num == meu:
    print('\n\33[32mParabéns, você acertou!\33[m')
print('\nO número q eu pensei foi \33[1;34m{}\33[m!'.format(num))
print('Foram necessárias \33[1;35m{}\33[m tentativa(s) para acertar!'.format(cont))
print('\33[36m-=-\33[m'*14)