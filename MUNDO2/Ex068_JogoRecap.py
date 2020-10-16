from random import randint
print('\n\33[1;34m', end = '')
print('=-'* 20)
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR?'))
print('=-'* 20)
print('\33[m')
vit = 0
while True:
    num = int(input('\nDiga um número de 0 a 10: '))
    maq = randint(0,10)
    res = num + maq
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
        print(f'Você jogou {num} e o computador {maq}. Total de {res} ', end = '')
        print('deu PAR' if res % 2 == 0 else 'deu ÍMPAR')
        if tipo == 'P':
            if res % 2 == 0:
                print('\nVocê venceu!')
                vit += 1
            else:
                print('\nVocê perdeu!')
                break
        elif tipo == 'I':
            if res % 2 == 1:
                print('\nVocê venceu!')
                vit += 1
            else:
                print('\nVocê perdeu!')
                break
        print('\nVamos jogar novamente...')
print(f'\nGAME OVER! Você ganhou {vit} vezes.')