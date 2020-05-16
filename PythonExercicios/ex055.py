pma = 0
pme = 0
for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        pma = peso
        pme = peso
    else:
        if peso > pma:
            pma = peso
        if peso < pme:
            pme = peso
print('{}kg maior peso e {}kg menor peso'.format(pma, pme))

