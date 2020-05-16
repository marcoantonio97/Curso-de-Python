from datetime import date
anonasc = int(input('Em qual ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para seu alistamento.'.format(saldo))
    print('Você precisará se alistar em {}'.format(saldo + anoatual))
else:
    saldo = idade - 18
    print('Já se passou {} ano(s) do seu alistamento.'.format(saldo))
    print('Você precisaria ter se alistado em {}'.format(anoatual - saldo))
