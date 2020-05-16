from math import hypot
catop = float(input('Digite o comprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa desse triângulo retângulo é igual a {:.2f}'.format(hypot(catop, catadj)))
'''hip = ((catadj**2) + (catop**2))**(1/2)
print('O comprimento da hipotenusa desse triângulo retângulo é igual a {:.2f}'.format(hip))'''
