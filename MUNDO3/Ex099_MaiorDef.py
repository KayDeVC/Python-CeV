from random import randint
def maior(*num):
    mai = cont = 0
    print('-=' * 21)
    print('Analizando os valores passados...')
    for valor in num:
        print(f'{valor}', end = ' ')
        if cont == 0 or valor > mai:
            mai = valor
        cont += 1
    print(f'Foram informados {cont} valores ao total.')
    print(f'O maior valor informado foi {mai}.')


maior(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior(randint(0,10), randint(0,10), randint(0,10))
maior(randint(0,10), randint(0,10))
maior(randint(0,10))
maior()