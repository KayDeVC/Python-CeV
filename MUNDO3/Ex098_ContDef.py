from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}:', flush = True)
    sleep(1)
    if i < f:
        c = i
        while c <= f:
            print(c, end = ' ', flush = True)
            sleep(0.5)
            c += p
        print('FIM')
    else:
        c = i
        while c >= f:
            print(c, end = ' ', flush = True)
            sleep(0.5)
            c -= p
        print('Fim')
    

print()
print('-=' * 21)
contador(1, 10, 1)
print('-=' * 21)
contador(10, 0, 2)
print('-=' * 21)
print('\nAgora é a sua vez,com sua contagem personalizada!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print()
print('-=' * 21)
contador(inicio, fim, passo)
print('-=' * 21)