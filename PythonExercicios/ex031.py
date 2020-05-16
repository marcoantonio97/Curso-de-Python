km = float(input('Qual é a distância da viagem (km)? '))
if km <= 200:
    print('A viagem custará R${:.2f}'.format(km * 0.50))
else:
    print('A viagem custará R${:.2f}'.format(km * 0.45))
