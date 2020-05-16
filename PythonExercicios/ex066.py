n = s = q = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    q += 1
print(f'De um total de {q} números, a soma deles é igual a {s}.')
