print('\n{:=^30}'.format(' SOMA PAR NO LAÇO '))
s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma entre os {} pares digitados é: {}'.format(cont, s))