def aumentar(n, a):
    res = n + (n * a / 100)
    return res


def diminuir(n, d):
    d /= 100
    n -= n * d
    return n


def dobro(num):
    num *= 2
    return num


def metade(num):
    num /= 2
    return num
