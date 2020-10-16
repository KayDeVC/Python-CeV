def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\33[1;31mERRO.Digite um número inteiro válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('O usuério preferiu não digitar esse número.')
            return 0
        else:
            return n


def leiafloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('\33[1;31mERRO.Digite um número inteiro válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('O usuério preferiu não digitar esse número.')
            return 0
        else:
            return n


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1} e o número real {n2}.')
