import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\33[31mO site pudim não está acessível bo momento.\33[m')
else:
    print('\33[33mConsegui acessar o site pudim com sucesso!\33[m')
