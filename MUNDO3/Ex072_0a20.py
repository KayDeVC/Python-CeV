tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
         	'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 
         	'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 
         	'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:     
    valor = int(input('\nDigite um valor de 0 a 20: '))
    if 0 <= valor <= 20:
        break
    print('Valor inválido. ', end = '')
print(f'\nVocê digitou o número {tupla[valor]}!')