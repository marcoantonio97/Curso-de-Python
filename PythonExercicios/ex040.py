nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
if media < 5.0:
    print('Com a média de {:.1f}, você está REPROVADO!'.format(media))
elif 5.0 < media < 6.9:
    print('Com a média de {:.1f}, você está de RECUPERAÇÃO!'.format(media))
else:
    print('Com a média de {:.1f}, você está APROVADO!'.format(media))
