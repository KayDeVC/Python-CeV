print('\n')
print('{:~^40}'.format(' SOMA RANDOM '))
num = soma = cont = 0
num = int(input('Digite um número: [999 para parar] '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: [999 para parar] '))
print('Foram digitados {} números e a soma deles é: {}'.format(cont, soma))
print('\nFIM DO PROGRAMA')