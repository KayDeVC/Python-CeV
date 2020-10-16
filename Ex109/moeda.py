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
