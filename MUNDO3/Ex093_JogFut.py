jogador = {}
gols = []
print()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} participou: '))
total = 0
for c in range(1, partidas + 1):
    tot = int(input(f' Quantos gols na partida {c}? '))
    total += tot
    gols.append(tot)
jogador['gols'] = gols[:]
jogador['total'] = total
print('-='*21)
print(jogador)
print('-='*21)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*21)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  -> Na partida {i+1} ele marcou {v} gols.')
print(f'Foi um total de {total} gols.')

#jogador['total'] = sum(gols)
#linha 19 "... {len(jogador['gols'])} partidas...
