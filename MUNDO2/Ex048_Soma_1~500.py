print('\n SOMA EM INTERVALOS SELETIVOS ')
s = 0
ct = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        ct += 1
print('A soma de todos os {} números ímpares, entre 1 e 500, múltiplos de 3 é igual á: \n\n{}'.format(ct, s))