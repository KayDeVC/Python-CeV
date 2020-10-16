print('\n\33[1;7;40mCALCULANDO IMC - ÍNDICE DE MASSA CORPORAL\33[m')
peso = float(input('Qual o seu peso? (Kg)'))
h = float(input('Qual a sua altura? (m)'))
imc = peso / (h ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \33[1;46mABAIXO DO PESO IDEAL\33[m!')
elif imc < 25:
    print('Você está no \33[1;42mPESO IDEAL\33[m!')
elif imc < 30:
    print('Você está em \33[1;43mSOBREPESO\33[m!')
elif imc < 40:
    print('Você está em estado de \33[1;31;43mOBESIDADE\33[m!')
else:
    print('Você está em estado de \33[1;33;41mOBESIDADE MÓRBIDA\33[m!')
