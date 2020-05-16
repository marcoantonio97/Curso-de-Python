'''from math import factorial
num = int(input('Digite um número: '))
print('O fatorial de {} é {}'.format(num, factorial(num)))'''
n = int(input('Digite um número: '))
c = n
f = 1
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')
