def área(l, c):
    area = l * c
    print(f'A área de um terreno com as dimensões {l}m x {c}m é de {area}m².')


lar = float(input('LARGURA (m): '))
cum = float(input('COMPRIMENTO (m): '))
área(lar, cum)
