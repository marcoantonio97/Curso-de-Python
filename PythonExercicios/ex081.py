valores = list()
while True:
    valores.append(int(input('Digite um número: ')))
    esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while esc not in 'NnSs':
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if esc in 'Nn':
        break
print(f'\n{len(valores)} valores foram digitados na lista.')
valores.sort(reverse=True)
print(f'A lista em ordenada em forma decrescente é: {valores}.')
if 5 in valores:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')
