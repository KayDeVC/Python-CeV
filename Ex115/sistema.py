from time import sleep

from Ex115.lib.arquivo import *

arq = 'Cadastro.txt'

if not arqexist(arq):
    criararq(arq)

while True:
    esc = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if esc == 1:
        lerarq(arq)
    elif esc == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif esc == 3:
        cabecalho('\33[31mFECHANDO O SISTEMA... ATÉ LOGO!\33[m')
        break
    else:
        print('\33[31mERRO: Digite uma opção válida!\33[m')
    sleep(1.5)
