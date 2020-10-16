print('\n{:-^40}'.format(' PESQUISA PARA O IBGE '))
somaidade = 0
medidade = 0
maioridh = 0
nomevelho = ''
m20 = 0
for c in range(0, 4):
    print('\nPessoa n° {}!'.format(c +1))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()[0]
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridh:
        maioridh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        m20 += 1
medidade = somaidade / 4
print('\nA média de idade do grupo é de {} anos.'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridh, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos!'.format(m20))