palavras = ('Procrastinar', 'Preguiça', 'Dormir', 'Jogar', 'Irritar', 'Comer', 'Beber')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
print('\n\nFIM DE PROGRAMA')