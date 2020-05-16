from random import randint
from time import sleep
computador = randint(0, 5)
usu = int(input('Tente descobrir o número escolhido: '))
print('CARREGANDO...')
sleep(1.5)
if computador == usu:
    print('Você acertou!')
else:
    print('Você errou!')
