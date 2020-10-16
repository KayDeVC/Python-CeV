def aumentar(n=0, a=0):
    res = n + (n * a / 100)
    return res


def diminuir(n=0, d=0):
    d /= 100
    n -= n * d
    return n


def dobro(num=0):
    num *= 2
    return num


def metade(num=0):
    num /= 2
    return num


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:5.2f}'.replace('.', ',')
