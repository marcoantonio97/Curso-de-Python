'''a = [2, 3, 6, 5]
#b = a #Faz uma ligação
b = a[:] #Copia todos os valores
b[2] = 4
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''





'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')'''



'''valores = list()
for c in range (0, 3):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')'''




num = [1, 2, 9, 4, 5]
#num[2] = 3
#num.append(7)
#num.sort(reverse=True)
num.insert(5, 6)
#num.pop()
#num.pop(0)
#if 7 in num:
#    num.remove(7)
#else:
#    print('Não achei o número 7.')
print(num)
#print('-'*30)
#print(f'Essa lista tem {len(num)} elementos')'''