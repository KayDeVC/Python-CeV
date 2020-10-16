import random
print('\n=====Humano vs máquina=====')
print('Estou pensando em um número de 0 a 5!')
num = random.randint(0,5)
meu = int(input('Qual número estou pensando?'))
if num == meu:
    print('Parabéns,Vc acertou!')
else:
    print('Errou feio,errou rude!')
print(num)
print('-=-'*10) #teste