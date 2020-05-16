v = float(input('Velocidade do veículo: '))
if v > 80:
    multa = (v - 80) * 7
    print('Você foi multado em: R${:.2f}'.format(float(multa)))
print('Dirija com segurança')
