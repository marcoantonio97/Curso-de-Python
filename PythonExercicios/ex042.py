seg1 = float(input('Segmento 1: '))
seg2 = float(input('Segmento 2: '))
seg3 = float(input('Segmento 3: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    if seg1 == seg2 == seg3:
        print('Este triângulo é um triângulo equilátero!')
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        print('Este triângulo é um triângulo isósceles!')
    elif seg1 != seg2 != seg3 != seg1:
        print('Este triângulo é um triângulo escaleno!')
else:
    print('Os segmentos informados NÃO PODEM forma um triângulo.')
