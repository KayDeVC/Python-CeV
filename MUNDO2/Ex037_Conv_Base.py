print('\n   CONVERSOR DE BASES  ')
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[1] para Binário\n[2] para Octal\n[3] para Haxadecimal')
esc = int(input('Sua escolha:'))
if esc == 1:
    print('\n{} convertido para Binário é {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('\n{} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('\n{} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('\n\33[1;31mEscolha inválida!\33[m')