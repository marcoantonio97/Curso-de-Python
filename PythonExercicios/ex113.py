def leiaInt(msg):
    while True:
        try:
            nint = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido: ')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados do usuário interrompida pelo usuário.')
            return 0
        else:
            return nint


def leiaFloat(msg):
    while True:
        try:
            nfloat = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número real válido: ')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados do usuário interrompida pelo usuário.')
            return 0
        else:
            return nfloat


nint = leiaInt('Digite um número inteiro: ')
nfloat = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {nint} e o número real {nfloat}.')
