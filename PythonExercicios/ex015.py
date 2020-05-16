dias = int(input('Dias alugados: '))
km = float(input('Quilômetros rodados: '))
print('Valor total a pagar R${:.2f}'.format((dias * 60) + (km * 0.15)))
