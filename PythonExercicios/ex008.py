m = float(input('Qual é a medida: '))
print('{:.0f}m equivale a {}km, {}hm, {}dam, {:.0f}dm, {:.0f}cm e {:.0f}mm'.format(m, (m/1000), (m/100), (m/10), (m*10), (m*100), (m*1000)))
