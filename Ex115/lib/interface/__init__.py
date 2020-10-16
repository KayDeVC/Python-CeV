def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\33[1;31mERRO -> Digite um número inteiro válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[31mO usuério preferiu não digitar esse número.\33[m')
            return 0
        else:
            return n


def linha(tam=45):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(45))
    print(linha())


def menu(lista):
    cabecalho('\33[33mMENU PRINCIPAL v1.0\33[m')
    c = 1
    for item in lista:
        print(f'\33[33m{c}\33[m - \33[34m{item}\33[m')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc
