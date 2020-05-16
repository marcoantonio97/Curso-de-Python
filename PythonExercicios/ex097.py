def escreva(txt):
    print('~' * (len(txt) + 2))
    print(f' {txt} ')
    print('~' * (len(txt) + 2))


texto = str(input('Escreva um texto: '))
escreva(texto)
