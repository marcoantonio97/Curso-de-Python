pessoa18 = homem = totm20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ''
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        pessoa18 += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        totm20 += 1
    esc = ''
    while esc not in 'SsNn':
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if esc in 'Nn':
        break
print(f'Há um total de {pessoa18} com mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'Há um total de {totm20} mulher(es) com menos de 20 anos.')
