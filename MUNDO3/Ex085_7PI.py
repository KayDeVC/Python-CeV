sete = [[], []]
print()
print(f'{" SETE VALORES ":=^40}')
for s in range(1, 8):
    num = int(input(f'Digite o {s}° valor: '))
    if num % 2 == 0:
        sete[0].append(num)
    elif num % 2 == 1:
        sete[1].append(num)
sete[0].sort()
sete[1].sort()
print(f'\nOs valores PARES digitados foram:\n{sete[0]}')
print(f'\nOs valores ÍMPARES digitados foram:\n{sete[1]}')