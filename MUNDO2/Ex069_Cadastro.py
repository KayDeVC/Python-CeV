print('\n', end = '')
maior = homem = mulher20 = 0
pes = 1
while True:
    print('~'*40)
    print('{:^40}'.format(f'CADASTRE a {pes} PESSOA'))
    print('~'*40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('~'*40)
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem +=1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    pes += 1
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]    
    if esc == 'N':
        break
print(f'\nTotal de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo foram cadastrados {homem} homens.')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')