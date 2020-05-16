preco = float(input('Preço atual do produto: R$'))
pag = int(input('Informe a forma de pagamento (0 - DINHEIRO, 1 - CHEQUE, 2 - CARTÂO): '))
if pag == 2:
    x = int(input('Infome o número de parcelas que serão feitas (1 - A vista, 2 - Duas vezes, 3 - Três vezes ou mais): '))

if pag != 2:
    print('Total a ser pago: R${:.2f}'.format(preco * 0.9))
elif x == 1:
    print('Total a ser pago: R${:.2f}'.format(preco * 0.95))
elif x == 2:
    print('Total a ser pago: R${:.2f}'.format(preco))
elif x == 3:
    print('Total a ser pago: R${:.2f}'.format(preco * 1.2))
else:
    print('Opção de Pagamento Inválida!')
