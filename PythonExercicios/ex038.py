n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primero número ({}) é o maior.'.format(n1))
elif n1 < n2:
    print('O segundo número ({}) é o maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais.')
