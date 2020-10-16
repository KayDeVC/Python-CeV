aluno = {}
print()
aluno['nome'] = str(input('Nome do Aluno: '))
aluno['média'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('*'*40)
for k, v in aluno.items():
    print(f' -> {k} é igual a {v}.')
