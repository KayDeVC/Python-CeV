from time import sleep
alunos = []
while True:
    nome = str(input('\nNome do Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Deseja continuar o cadastro? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
print()
print('-='*20)
print(f'{"No.":<4}{"Aluno":^10}{"Média":>8}')
print('-'*35)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:^10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(1.5)
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são: {alunos[opc][1]}.')
print('<<<<< VOLTE SEMPRE >>>>>')