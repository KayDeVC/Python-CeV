from datetime import date
print('\n  EXERCÍTO BRASILEIRO  ')
nasc = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
idade = atual - nasc
if idade < 18:
    saldo = 18 - idade
    alis = nasc + 18
    print('\nAinda faltam {} anos para você se alistar!'.format(saldo))
    print('Seu alistamento será em {}!'.format(alis))
elif idade == 18:
    print('\nCompareça a Junta Militar mais próxima! Hora de de alistar!')
else:
    saldo = idade - 18
    alis = nasc +18
    print('\nJá se passou {} ano(s) do seu alistamento obrigatório!'.format(saldo))
    print('Seu alistamento foi em {}!'.format(alis))