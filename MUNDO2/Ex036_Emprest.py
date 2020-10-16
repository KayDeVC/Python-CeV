print('\n\33[4;32m+#+#+# FINANCIAMENTO CAIXA #+#+#+\33[m')
casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário atualmente? R$'))
ano = int(input('Em quantos anos você irá pagar? '))
prest = casa / (ano *12)
psal = sal * 0.3
print('\nPara pagar uma casa de \33[33mR${:.2f}\33[m em \33[34m{}\33[m anos, cada prestação será de \33[35mR${:.2f}\33[m'.format(casa, ano, prest))
if psal >= prest:
    print('\33[1;32mEmpréstimo Aprovado\33[m!')
elif psal < prest:
    print('\33[1;31mEmpréstimo RECUSADO\33[m!')