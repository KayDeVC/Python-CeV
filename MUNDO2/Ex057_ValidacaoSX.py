print('\n{:+^40}'.format(' VALIDAÇÃO DE DADOS '))
r = str(input('Qual é o seu sexo?: [M/F] ')).upper().strip()[0]
while r not in 'FM':
    r = str(input('Dado inválido, digite seu sexo: [M/F] ')).upper().strip()[0]
print('\nSexo {} registrado com sucesso'.format(r))