print()
num = []
maior = menor = 0
for n in range(0, 5):
    num.append(int(input(f'Digite um número na posição {n}: ')))
    if n == 0:
        maior = menor = num[n]
    else:
        if num[n] > maior:
            maior = num[n]
        if num[n] < menor:
            menor = num[n]
print('-='*21)
print(f'Você digitou os valores {num}.')           
print(f'O maior valor foi {maior} nas posições ', end = '')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end = '')
print()
print(f'O menor valor foi {menor} nas posições ', end = '')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end = '')
print()