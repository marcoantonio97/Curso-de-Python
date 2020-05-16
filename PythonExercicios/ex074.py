from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados são: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi: {max(n)}.')
print(f'O menor valor sorteado foi: {min(n)}.')
