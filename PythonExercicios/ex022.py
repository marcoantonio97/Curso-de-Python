nome = input('Digite o seu nome completo: ').strip()
print('O nome com todas as letras maísuculas é: {}'.format(nome.upper()))
print('O nome com todas as letras minusculas é: {}'.format(nome.lower()))
print('Total de letras sem espaços: {}'.format(len(nome)-nome.count(' ')))
print('Total de letras do primeiro nome: {}'.format(nome.find(' ')))
