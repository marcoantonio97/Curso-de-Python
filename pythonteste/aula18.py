'''dados = list()
dados.append('Pedro')
dados.append(25)
pessoas = list()
pessoas.append(dados[:])
dados[0] = 'Maria'
dados[1] = 19
pessoas.append(dados[:])
print(pessoas)
'''

'''pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print('-'*30)
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

galera = list()
dados = list()
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
'''print(galera)'''
totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maior(es) e {totmen} menor(es) de idade.')
