val = (int(input('\nDigite um valor: ')),
	      int(input('Digite outro valor: ')),
	      int(input('Digite mais um valor: ')),
	      int(input('Digite o último valor: ')))
print(f'Você digitou os valores: {val}')
print(f'O valor 9 apareceu {val.count(9)} vezes.')
if 3 in val:
    print(f'O valor 3 apareceu na {val.index(3)+1}a posição.')
else:
    print('O valor 3 não foi digitado nenhuma vez!')
print('Os valores pares digitados foram: ', end = '')
for v in val:
    if v % 2 == 0:
        print(v, end = ' ')