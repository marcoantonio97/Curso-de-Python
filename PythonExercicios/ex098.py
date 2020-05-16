from time import sleep


def contador(inicio, fim, passo):
    if fim > inicio:
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end=' ')
            sleep(0.5)
        print('FIM')
    elif fim < inicio and passo > 0:
        passo *= -1
        for c in range(inicio, fim - 1, passo):
            print(f'{c}', end=' ')
            sleep(0.5)
        print('FIM')
    elif fim < inicio and passo < 0:
        for c in range(inicio, fim - 1, passo):
            print(f'{c}', end=' ')
            sleep(0.5)
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem Personalizada')
i = int(input('Digite o número inicial: '))
f = int(input('Digite o número final: '))
p = int(input('Digite o passo que ele deve pular: '))
if p == 0:
    p = 1
contador(i, f, p)
