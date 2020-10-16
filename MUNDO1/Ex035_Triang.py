print('\n===== TRIÂNGULOS ======')
a = float(input ('Qual a medida da primeira reta? '))
b = float(input('Qual a medida da segunda reta? '))
c = float(input('Qual a medida da terceira reta? '))
if a < b + c and b < a + c and c < a + b:
    print('As retas \33[32mpodem formar\33[m um triângulo!')
else:
    print('As retas \33[31mNÃO PODEM\33[m formar um triângulo!')

#(b - c) < \\ (a - c) < \\ (a - b) <