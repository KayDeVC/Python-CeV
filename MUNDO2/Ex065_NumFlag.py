print('\n<---> Fabricando números <--->\n')
esc = 'S'
soma = qt = med = maior = menor = 0
while esc in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qt += 1
    if qt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    esc = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
med = soma / qt
print('\nA média dos {} valores digitados é: {:.2f}'.format(qt, med))
print('O maior número foi {} e o menor número foi {}.'.format(maior, menor))