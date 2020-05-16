from random import randint
from time import sleep
computador = randint(0, 10)
acertou = False
tent = 0
while not acertou:
    usu = int(input('Descubra o número escolhido: '))
    print('CARREGANDO...')
    sleep(0.5)
    tent += 1
    if computador == usu:
        print('Você acertou!')
        acertou = True
    else:
        if usu < computador:
            print('Você errou. Tente um valor maior. ', end='')
        else:
            print('Você errou. Tente um valor menor. ', end='')
print('Você precisou de {} tentativas para descobrir.'.format(tent))
