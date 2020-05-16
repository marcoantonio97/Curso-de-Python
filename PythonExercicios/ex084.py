geral = list()
pessoa = list()
kmaior = kmenor = 0
pesada = list()
leve = list()
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    geral.append(pessoa[:])
    if kmaior == 0 and kmenor == 0:
        kmaior = pessoa[1]
        pesada.append(pessoa[0])
        kmenor = pessoa[1]
        leve.append(pessoa[0])
    else:
        if pessoa[1] > kmaior:
            pesada.clear()
            kmaior = pessoa[1]
            pesada.append(pessoa[0])
        elif pessoa[1] == kmaior:
            pesada.append(pessoa[0])
        elif pessoa[1] < kmenor:
            leve.clear()
            kmenor = pessoa[1]
            leve.append(pessoa[0])
        elif pessoa[1] == kmenor:
            leve.append(pessoa[0])
    pessoa.clear()
    esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while esc not in 'NnSs':
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if esc in 'Nn':
        break
print(f'Total de pessoas cadastradas: {len(geral)}.')
print(f'Com o peso de {kmaior}kg, {pesada} é(são) o(s) mais pesado(s).')
print(f'Com o peso de {kmenor}kg, {leve} é(são) o(s) mais leve(s).')
