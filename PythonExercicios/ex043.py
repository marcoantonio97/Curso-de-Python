peso = float(input('Qual é o seu peso? '))
alt = float(input('Qual é a sua altura? '))
imc = peso / (alt**2)
if imc < 18.5:
    print('Com o IMC igual a {:.1f}, você está ABAIXO DO PESO!'.format(imc))
elif imc < 25:
    print('Com o IMC igual a {:.1f}, você está no PESO IDEAL!'.format(imc))
elif imc < 30:
    print('Com o IMC igual a {:.1f}, você está com SOBREPESO!'.format(imc))
elif imc < 40:
    print('Com o IMC igual a {:.1f}, você está com OBESIDADE!'.format(imc))
else:
    print('Com o IMC igual a {:.1f}, você está com OBESIDADE MÓRBIDA!'.format(imc))
