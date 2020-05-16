valores = list()
while True:
    valores.append(int(input('Digite um número: ')))
    esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while esc not in 'NnSs':
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if esc in 'Nn':
        break
pares = list()
impares = list()
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Lista Completa: {valores}')
print(f'Números Pares: {pares}')
print(f'Números Ímpares: {impares}')
