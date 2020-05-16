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

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc