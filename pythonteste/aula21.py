'''
def contador (i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :Parâmetro i: inicio da contagem.
    :Parãmetro f: fim da contagem.
    :Parãmetro p: passo da contagem.
    :Return: sem retorno
    """

    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')

help(contador)

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 2, 5)
somar(8, 4)
'''

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return  s
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)

print(f'Os resultados são {r1}. {r2}, {r3}.')
