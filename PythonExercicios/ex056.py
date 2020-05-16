somaidade = 0
mediaidade = 0
maioridadehomem = 0
nhvelho = ''
totm20 = 0
for p in range(1, 5):
    nome = str(input('Digite seu nome completo: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nhvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nhvelho = nome

    if sexo in 'Ff' and idade < 20:
        totm20 += 1

mediaidade = somaidade // 4
print('A média de idade de todos é {} anos'.format(mediaidade))
print('{} é o homem mais velho, com {} anos.'.format(nhvelho, maioridadehomem))
print('Há um total de {} mulher(es) com menos de 20 anos.'.format(totm20))
