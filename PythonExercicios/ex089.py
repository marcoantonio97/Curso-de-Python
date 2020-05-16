ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while esc not in 'NnSs':
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if esc in 'Nn':
        break
print('-=-' * 30)
print(f'{"Nº.":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    resp = int(input('Mostrar as notas de qual aluno (999 para sair): '))
    if resp == 999:
        break
    if resp <= len(ficha) -1:
        print(f'Notas de {ficha[resp][0]} são {ficha[resp][1]}')
