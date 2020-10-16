from time import sleep
from random import randint
print()
print('-+-'*13)
print(f'{"JOGUE NA MEGA SENA":^40}')
print('-+-'*13)
mega = [] #lista principal
aux = [] #lista auxiliar
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in aux: #conferindo se o número é duplicado
            aux.append(num) #adiciona na lista auxiliar
            cont += 1
        if cont >= 6:
            break
    aux.sort() #ordena lista
    mega.append(aux[:]) #copia para a lista principal
    aux.clear() #apaga lista auxiliar
    tot += 1
print()
print('-='*4, f'SORTEANDO OS {jogos} JOGOS', '-='*4)
for i, j in enumerate(mega):
    print(f'Jogo {i+1}: {j}')
    sleep(1)
print()
print('*"'*7, 'BOA SORTE', '*"'*7)