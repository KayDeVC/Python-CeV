print('CADEIA DE TEXTOS')
nome = str(input('Digite o seu nome completo:')).strip()
print('Seu nome somente em maiúsculas:',nome.upper())
print('Seu nome somente em minúsculas:',nome.lower())
nome2 = nome.replace(' ','')
print('Seu nome tem {} letras ao todo.'.format(len(nome2)))
div = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(div[0])))

print('MELHORADO')
print('Cont. de letras sem espaço: {}.'.format(len(nome)-nome.count(' ')))
print('Cont. de letras no 1° nome: {}.'.format(nome.find(' ')))