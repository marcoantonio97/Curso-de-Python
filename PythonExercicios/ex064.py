num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print('O total de números digitados foi {} que somados é igual a {}.'.format(cont, soma))
