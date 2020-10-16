print('\n{:=^40}'.format(' PALÍNDROMO '))
frase = str(input('Digite uma frase: ')).strip().upper()
part = frase.split()
junto = ''.join(part)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}!'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase não é um Palindromo!')

inverso2 = junto[::-1]
print(inverso2)