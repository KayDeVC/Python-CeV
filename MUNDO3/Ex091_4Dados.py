from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = []
print('$'*40)
print(f'{"QUE ROLEM OS DADOS":^40}')
print('#'*40)
for c in range(1, 5):
    jogo[f'Jogador {c}'] = randint(1, 6)
for k, v in jogo.items():
    print(f'         -> {k} jogou {v}.')
    sleep(1)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print('$'*40)
print(f'{"RANKING DOS PARTICIPANTES":^40}')
print('#'*40)
for i, v in enumerate(ranking):
    print(f'   -> {i+1}° Lugar: {v[0]} com {v[1]}.')
    sleep(1)
print(f'\n{"FIM DE JOGO":^40}')

#jogo = {'Jogador 1': randint(1, 6),
#        'Jogador 2': randint(1, 6),
#        'Jogador 3': randint(1, 6),
#        'Jogador 4': randint(1, 6)}
