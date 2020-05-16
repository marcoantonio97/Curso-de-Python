nome = str(input('Digite seu nome completo: ')).strip()
nnome = nome.split()
print('Seu primeiro nome é: {}'.format(nnome[0]))
print('Seu último nome é: {}'.format(nnome[len(nnome)-1]))
