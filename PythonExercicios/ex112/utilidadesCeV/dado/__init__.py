def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".")
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: \"{entrada}\" é um valor inválido!')
        else:
            valido = True
            return float(entrada)