brasileirao = ('Palmeiras', 'Flamengo', 'Inter', 'SP', 'Grêmio', 'CAM', 'Santos', 'CAP', 'Cruzeiro', 'Fluminense', 'Corinthians',
               'Bahia', 'Ceará', 'Vasco', 'Botafogo', 'América-MG', 'Chapecoense', 'Sport', 'Vitória', 'Paraná')

print(f'Os primeiros 5 colocados do campeonato são: {brasileirao[:5]}')
print(f'Os últimos 4 colocados do campeonato são: {brasileirao[-4:]}')
print(f'Os times em ordem alfabética: {sorted(brasileirao)}')
print(f'A Chapecoense está na {brasileirao.index("Chapecoense")+1}º colocação.')
