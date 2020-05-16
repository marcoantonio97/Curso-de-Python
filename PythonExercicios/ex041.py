from datetime import date
anonasc = int(input('Em qual ano você nasceu? '))
ano = date.today().year
idade = ano - anonasc
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
