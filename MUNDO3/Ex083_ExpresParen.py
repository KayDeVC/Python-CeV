exp = str(input('Digite a expressão matemática: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\nSua expressão ESTÁ correta!')
else:
    print('\nSua expressão NÃO está correta!')
