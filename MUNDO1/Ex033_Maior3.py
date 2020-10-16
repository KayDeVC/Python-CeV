print('\n==== MAIOR/MENOR ====')
num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
num3 = float(input('Dugite o terceiro número:'))
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('\nO maior número é: {}!'.format(maior))
print('O menor número é: {}!'.format(menor))