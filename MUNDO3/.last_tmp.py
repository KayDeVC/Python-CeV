def fatorial(n, show = False):
    """
      => Calcula o valor do fatorial do número.
      :param n: O número a ser calculado.
      :param show: (opcional) Mostrar ou não a conta.
      :return: O valor fatorial do número n.
    """
    cont = n
    fat = 1
    while cont > 0:
        if show:
            print(f'{cont}', end = '')
            print(' x ' if cont > 1 else ' = ', end = '')
        fat *= cont
        cont -= 1
    return fat
        

num = int(input('Número para calcular o fatorial: '))
print(fatorial(num, ))
help(fatorial)