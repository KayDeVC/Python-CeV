print(' REAL X DÓLAR ')
real = float(input('Quantos reais vc tem na carteira? R$'))
dolar = real / 3.27
print('Você pode comprar US${:.2f} com seus R${:.2f}'.format(dolar, real))