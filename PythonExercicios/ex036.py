casa = float(input('Valor da Casa: R$'))
salario = float(input('Valor do salário: R$'))
tempo = int(input('Quantos anos para pagar: '))

prest = casa / (tempo * 12)
prestmax = salario * 0.3

if prest > prestmax:
    print('Como o valor da prestação R${:.2f} ultrapassa o limite de 30% do salário (R${:.2f}), o empréstimo foi negado!'.format(prest, prestmax))
else:
    print('Empréstimno aprovado!')
