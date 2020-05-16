estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Fed.: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)



'''pessoas = {'nome': 'Marco', 'idade': 21, 'Sexo': 'M'}
pessoas['nome'] = 'Alexandre'
pessoas['peso'] = 60.5
print(pessoas)
'''
'''
brasil = []
est1 = {'UF': 'São Paulo', 'sigla': 'SP'}
est2 = {'UF': 'RJ', 'sigla': 'RJ'}
brasil.append(est1)
brasil.append(est2)
print(brasil[0]['UF'])
'''

'''dados = dict()
dados = {'nome':'Pedro', 'idade': 25}
dados['sexo'] = 'M'
del dados['idade']
print(dados)


filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())
print('-'*10)
print(filme.keys())
print('-'*10)
print(filme.items())
print('-'*40)

for k, v in filme.items():
    print(f'O {k} é {v}.')
'''