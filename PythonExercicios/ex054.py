from datetime import date
atual = date.today().year
s = 0
for c in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        s = s + 1
print('{} não atingiram a maioridade e {} já atingiram a maioridade.'.format(7 - s, s))
