grupo = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MmFf':
            break
        print('ERRO! Digite um sexo válido [M/F].')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp in 'SsNn':
            break
        print('ERRO! Digite uma opção válida [S/N].')
    if resp == 'N':
        break
print('=' * 40)
print(f'Ao todo foram cadastradas {len(grupo)} pessoas.')
media = soma / len(grupo)
print('=' * 40)
print(f'A média de idade é de {media:5.2f}.')
print('=' * 40)
print('As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print('=' * 40)
print('Lista de Pessoas com Idade acima da Média:')
for p in grupo:
    if p['Idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}')
