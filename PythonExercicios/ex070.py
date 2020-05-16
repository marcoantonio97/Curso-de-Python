tot = prod1000 = barato = 0
nomp = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip().title()
    preco = float(input('Digite o valor do produto: R$'))
    tot += preco

    if preco > 1000:
        prod1000 += 1

    if barato == 0:
        barato = preco
        nomp = nome
    elif preco < barato:
        barato = preco
        nomp = nome

    esc = ''
    while esc not in 'SsNn':
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if esc in 'Nn':
        break
print(f'Total gasto na compra: R${tot:.2f}')
print(f'Total de itens com valor superior a R$1000: {prod1000}')
print(f'Com o valor de R${barato:.2f}, {nomp} é o produto mais barato.')
