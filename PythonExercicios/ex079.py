valores = list()
while True:
    v = int(input('Digite um número: '))
    if v not in valores:
        valores.append(v)
    else:
        print(f'O valor {v} já está adicionado a lista. ', end='')
    esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while esc not in 'NnSs':
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if esc in 'Nn':
        break
valores.sort()
print(f'Os valores informados em ordem crescente são: {valores}.')
