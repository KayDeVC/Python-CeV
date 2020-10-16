num = []
while True:
    num.append(int(input('\nDigite um número: ')))
    esc: str = ' '
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
num.sort(reverse=True)
print()
print ( '-+' * 21 )
print(f'\nVocê digitou {len(num)} valores.')
print(f'\nOs Números digitados em ordem decrescente foram:  {num}')
if 5 in num:
    print('\nO número 5 FAZ parte da lista!')
else:
    print('\nO número 5 NÃO faz parte da lista!')

#Usei no meu método, contador.