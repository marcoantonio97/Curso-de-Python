resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
media = soma / quant
print('Você digitou {} números e a média deles é igual a {}.'.format(quant, media))
print('O maior número informado foi {} e o menor número informado foi {}.'.format(maior, menor))
