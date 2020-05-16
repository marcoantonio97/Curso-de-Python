from random import randint


def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))

def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares é igual a: {soma}')


num = list()
sorteia(num)
print(num)
somaPar(num)
