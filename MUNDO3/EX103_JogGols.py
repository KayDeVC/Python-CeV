def ficha(j='<desconhecido>', g=0):
    print(f'O jogador {j}, fez {g} gol(s) no campeonato.')


jog = str(input('Nome do Jogador: '))
gol = str(input('Quantos gols ele marcou? '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jog.strip() == '':
    ficha(g=gol)
else:
    ficha(jog, gol)
