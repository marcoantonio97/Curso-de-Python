from random import randint
from time import sleep
computador = randint(0, 2)
usuario = int(input('Escolha sua opção (0 - Pedra, 1 - Papel, 2 - Tesoura): '))
print('CARREGANDO...')
sleep(1)
if usuario == computador:
    print('Você escolheu {} e o computador escolheu {}, o jogo deu empate.'.format(usuario, computador))
elif computador == 0 and usuario == 1:
    print('Computador escolheu {}-Pedra e você escolheu {}-Papel, você ganhou!!'.format(computador, usuario))
elif computador == 0 and usuario == 2:
    print('Computador escolheu {}-Pedra e você escolheu {}-Tesoura, você perdeu!!'.format(computador, usuario))
elif computador == 1 and usuario == 0:
    print('Computador escolheu {}-Papel e você escolheu {}-Pedra, você perdeu!!'.format(computador, usuario))
elif computador == 1 and usuario == 2:
    print('Computador escolheu {}-Papel e você escolheu {}-Tesoura, você ganhou!!'.format(computador, usuario))
elif computador == 2 and usuario == 0:
    print('Computador escolheu {}-Tesoura e você escolheu {}-Pedra, você ganhou!!'.format(computador, usuario))
elif computador == 2 and usuario == 1:
    print('Computador escolheu {}-Tesoura e você escolheu {}-Papel, você perdeu!!'.format(computador, usuario))
