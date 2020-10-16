matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = c3 = mai = 0
print(f'{" MATRIZ 2.0 ":=^40}')
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[l][2]:
            c3 += matriz[l][2]
        if matriz[1][c] == 0:
            mai = matriz[1][c]
        else:
            if matriz[1][c] > mai:
                mai = matriz[1][c]           
print('-='*21)
print()
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print()
print('-='*21)
print(f'\nA soma dos valores pares é: {somapar}')
print(f'A soma dos valores da terceira coluna é:\n{c3}')
print(f'E o maior valor da segunda linha é: {mai}')
