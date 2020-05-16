'''print('-' * 30)
print('            PYTHON            ')
print('-' * 30)


def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('           PYTHON')



def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A e B é igual a {s}')
    print()


soma(4, 5)
soma(8, 9)
soma(2, 1)



def contador(*num):
    print(num)
    print()


numeros = list()
for n in range(0, 5):
    numeros.append(int(input(f'Número {n}: ')))
contador(numeros)
contador(5, 1, 7, 5, 9, 3, 4, 5)
contador(5, 0)
'''


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
