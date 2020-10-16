from time import sleep
from datetime import date
print('=======O ANO É BISSEXTO?=======')
ano = int(input('Diga um ano para eu analisar: \nColoque 0 para analisar o ano atual!'))
print('PROCESSANDO...')
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Sim! O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} NÃO é Bissexto!'.format(ano))