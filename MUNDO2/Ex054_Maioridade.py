from datetime import date
print('\n{:=^40}'.format(' MAIORIDADE '))
atual = date.today().year
mai = 0
men = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento {}:'.format(c)))
    idade = atual - nasc
    if idade >= 21:
        mai += 1
    elif idade < 21:
        men += 1        
print('\nO número de pessoas maiores de idade é:', mai)
print('\nO número de pessoas que ainda não atingiram a maioridade é:', men)