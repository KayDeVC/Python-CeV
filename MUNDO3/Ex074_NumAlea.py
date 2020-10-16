from random import randint
num = (randint(1,10), randint(1,10), randint(1,10),
       randint(1,10), randint(1,10))
print('\n', end = '')
print('Os valores sorteados foram: ', end = '')
for n in num:    
    print(f'{n} ', end = '')
print(f'\nO maior número foi: {max(num)}')
print(f'O menor número foi: {min(num)}')