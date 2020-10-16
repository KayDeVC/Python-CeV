def aumentar(n=0, a=0, formato=False):
    res = n + (n * a / 100)
    return res if formato is False else moeda(res)


def diminuir(n=0, d=0, formato=False):
    d /= 100
    n -= n * d
    return n if not formato else moeda(n)


def dobro(num=0, formato=False):
    num *= 2
    return num if not formato else moeda(num)


def metade(num=0, formato=False):
    num /= 2
    return num if not formato else moeda(num)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:5.2f}'.replace('.', ',')


def resumo(preco=0, taxa=10, tx=0):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Dobro do Preço: \t{dobro(preco, True)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'Com {taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'Com {tx}% de Redução: \t{diminuir(preco, tx, True)}')
    print('-'*30)
