maior = 0
menor = 0
print('\n{:=^32}'.format(' QUEM PESA MAIS/MENOS? '))
for c in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg!'.format(maior))
print('E o menor peso lido foi de {}kg!'.format(menor))