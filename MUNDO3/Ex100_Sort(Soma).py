from random import randint
from time import sleep

def sorteio(lista):
    print(f'Sorteando os valores: ', end = '', flush = True)
    sleep(1)
    for num in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(n, end = ' ', flush = True)
        sleep(0.4)
    print('PRONTO')
    

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de\n{lista} temos o resultado: {soma}.')
        
    
numeros = []
print()
print('$+' * 21)
sorteio(numeros)
print()
somapar(numeros)