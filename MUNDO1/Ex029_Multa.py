from time import sleep
print('\n')
print('=+'*15)
print('O limite de velocidade é de 80km/h...')
vel = int(input ('Qual a sua velocidade agora? '))
if vel > 80:
    multa = (vel-80)*7
    print('Bonito, hein...')
    sleep(1.5)
    print('Você será multado em: R${:.2f}'.format(multa))
else:
    print('Parabéns, Vc é um exemplo de pessoa!')