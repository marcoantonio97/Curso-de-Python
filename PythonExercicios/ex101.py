from datetime import  datetime
def voto(a):
    ano = datetime.now().year
    idade = ano - a
    if (idade < 16):
        print(f'Com {idade} anos, o voto está NEGADO')
    elif (16 <= idade and idade < 18) or idade > 65:
        print(f'Com {idade} anos, o voto está OPCIONAL')
    else:
        print(f'Com {idade} anos, o voto está OBRIGATÓRIO')


ano = int(input('Em que ano você nasceu: '))
voto(ano)
