valores = []
for v in range(0, 5):
    val = int(input('\nDigite um valor: '))
    if v == 0 or val > valores[-1]:
        valores.append(val)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if val <= valores[pos]:
                valores.insert(pos, val)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print()
print('*-'*21)
print(f'\nVocê digitou os valores {valores}.')