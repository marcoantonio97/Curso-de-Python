palavras = ('Celular', 'Garrafa', 'Computador', 'Monitor', 'Notebook', 'Mochila', 'Mouse', 'Caixa', 'Papel', 'Armario', 'Caneta')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra in 'AaEeIiOoUu':
            print(letra, end=' ')
