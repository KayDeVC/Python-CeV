print('+++> AUMENTO DE SALÁRIO <+++')
sal = float(input('Digite o salário atual: R$'))
if sal > 1250:
    aum = '10%'
    novsal = sal * 1.1
else:
    aum = '15%'
    novsal = sal * 1.15
print('Seu novo salário, com aumento de {} é R${:.2f}!'.format(aum, novsal))