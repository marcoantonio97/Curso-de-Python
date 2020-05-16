lanche  = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche))
print('-'*50)

for comida in lanche:
    print(f'Eu vou comer {comida}.')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

print('-'*50)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(5))
print('-'*50)
pessoa = ('Marco', 21)
del(pessoa)
print(pessoa)
