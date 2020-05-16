jogador = dict()
partidas = []
jogador['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['Gols'] = partidas.copy()
jogador['Total'] = sum(partidas)
print('='*40)
print(jogador)
print('='*40)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('='*40)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i + 1} ele fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gol(s).')
