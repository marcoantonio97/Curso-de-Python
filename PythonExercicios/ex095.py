time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['Gols'] = partidas.copy()
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SsNn':
            break
        print('ERRO! Digite uma opção válida [S/N].')
    if resp in 'Nn':
        break
print('='*40)
print('Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*40)

while True:
    busca = int(input('Mostrar os dados de qual jogador? [999 para interromper]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com o código {busca}.')
    else:
        print(f'Jogador {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
