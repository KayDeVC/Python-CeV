galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. Digite apenas "M" ou "F".')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        esc = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if esc in 'SN':
            break
        print('ERRO. Digite apenas "S" ou "N".')
    if esc == 'N':
        break
print('-='*21)
print(f'A) Ao todo temos {len(galera)} de pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idades das pessoas é de {media:5.2f}.')
print('C) As mulheres cadastradas foram: ', end = '')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end = ' ')
print()
print('D) As pessoas acima da média de idade são: ')
for p in galera:
    if p['idade'] >= media:
        print('  ', end = '')
        for k,v in p.items():
            print(f'{k} = {v}: ', end = '')
        print()
print('<<<<<<< ENCERRANDO >>>>>>>')