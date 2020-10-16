print('\n')
print('{:~^40}'.format(' SOMA RANDOM '))
num = soma = cont = 0
while True:
    num = int(input('Digite um número: [999 para parar] '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'\nForam digitados {cont} números e a soma deles é: {soma}')
print('\nFIM DO PROGRAMA')