from random import randint
v = soma = 0
while True:
    computador = randint(0, 10)
    usunum = int(input('Digite seu número: '))
    soma = computador + usunum
    usuescolha = ''
    while usuescolha not in 'PpIi':
        usuescolha = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    if usuescolha in 'Pp':
        if soma % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif soma % 2 != 0:
        print('Você venceu!')
        v += 1
    else:
        print('Você perdeu!')
        break
print(f'Número de vitórias consecutivas: {v}')
