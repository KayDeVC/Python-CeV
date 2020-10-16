print('\n{:=^40}'.format(' FORMA DE PAGAMENTO? '))
valor = float(input('Qual o valor da compra? R$'))
print('''Qual a forma de pagamento?
[ 1 ] Dinheiro/Cheque á vista
[ 2 ] Cartão á vista
[ 3 ] 2 x no cartão
[ 4 ] 3 x ou mais no cartão''')
opc = int(input('Sua opção: '))
if opc == 1:
    valf = valor * 0.9
    print('Sua compra que custava R${:.2f}, com desconto de 10% será R${:.2f}!'.format(valor, valf))
elif opc == 2:
    valf = valor * 0.95
    print('Sua compra que custava R${:.2f}, com desconto de 5% será R${:.2f}!'.format(valor, valf))
elif opc == 3:
    valf = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f}!'.format(valf))
elif opc == 4:
    parc = int(input('Quantas parcelas? '))
    valf = valor * 1.2
    vpar = valf / parc
    print('Sua compra com juros de 20%, será R${:.2f} em {} parcelas de R${:.2f}.'.format(valf, parc, vpar))
else:
    print('\n\33[1;33;41mCOMANDO INVÁLIDO, REINICIE O PROGRAMA\33[m!')