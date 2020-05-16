from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo desejado: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('Para o ângulo {}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(ang, seno, cosseno, tangente))
