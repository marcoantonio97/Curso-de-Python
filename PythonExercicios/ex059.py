m = 1
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
while m != 0:
    print('''
Você deseja:
[1] Somar
[2] Multiplicar
[3] Maior entre eles
[4] Digitar novos valores
[5] Sair do programa
    ''', end='')
    escolha = int(input('''
Escolha: '''))
    if escolha == 1:
        print('A soma entre os valores é igual a: {}'.format(num1 + num2))
    if escolha == 2:
        print('O produto dos valores é igual a: {}'.format(num1 * num2))
    if escolha == 3:
        if num1 > num2:
            print('O maior valor entre os informados é: {}'.format(num1))
        else:
            print('O maior valor entre os informados é: {}'.format(num2))
    if escolha == 4:
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
    if escolha == 5:
        m = 0
