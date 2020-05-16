num = int(input('Digite um número: '))
opcao = int(input('Escolha a opção de conversão do número (1 - Binário, 2 - Octal, 3 - Hexadecimal): '))
if opcao == 1:
    print('O número {} em binário é igual a {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em octal é igual a {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida')
