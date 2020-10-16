from datetime import date
print('\n\33[1;34m=> CNN - CONFEDERAÇÃO NACIONAL DE NATAÇÃO <=\33[m')
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
print('\nO atleta em {} anos.'.format(idade))
if idade <= 9:
    print('\33[1;32mClassificação: MIRIM\33[m')
elif idade <= 14:
    print('\33[1;32mClassificação: INFANTIL\33[m')
elif idade <= 19:
    print('\33[1;32mClassificação: JÚNIOR\33[m')
elif idade <= 25:
    print('\33[1;32mClassificação: SÊNIOR\33[m')
else:
    print('\33[1;32mClassificação: MASTER\33[m')