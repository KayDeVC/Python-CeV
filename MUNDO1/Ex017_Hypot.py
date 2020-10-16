import math
print('+++Cálculo da Hipotenusa+++')
ca = float(input('Comprimento do Cateto Adjacente:'))
co = float(input('Comprimento do Cateto Oposto:'))
h = ((ca**2)+(co**2))**(0.5)
print('O comprimento da Hipotenusa é: {:.2f}!'.format(h))

print('MELHORADO')
h2 = math.hypot(ca,co)
print('Hipotenusa vale: {:.3f}.'.format(h2))