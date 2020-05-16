num = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))

print(f'O número 9 apareceu {num.count(9)} vez(es).')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores digitados pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')
