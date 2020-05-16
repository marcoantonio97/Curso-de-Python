n = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print('{} x {:2} = {:2}'.format(n, c, (n * c)))
    print('-'*15)
