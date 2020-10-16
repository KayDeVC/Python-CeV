from time import sleep
print('#-+'*5)
print('Latan viagens... Aguarde...')
sleep(2)
dist = float(input('Qual a distância a ser percorrida?'))
print('PROCESSANDO...')
sleep(2)
if dist <= 200:
    p1 = dist*0.5
    print('Sua passagem custará R${:.2f}'.format(p1))
else:
    p2 = dist*0.45
    print('Sua passagem custará R${:.2f}'.format(p2))
print('LATAN AGRADECE SUA ESCOLHA')
print('VOLTE SEMPRE!!')
print('+-#'*5)