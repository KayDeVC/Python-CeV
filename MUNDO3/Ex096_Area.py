def area(a, b):
    res = a * b
    print(f'A área de um terreno {a:.1f}m x {b:.1f}m é de\n {res:.2f}m²')


print()
print(f'{"Controle de terrenos":^40}')
print('-'*40)
larg = float(input('Largura: (m) '))
comp = float(input('Comprimento: (m) '))
area(larg, comp)
