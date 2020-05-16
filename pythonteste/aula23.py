try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Problemas no tipo de dados digitados.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário abortou o preenchimento dos dados.')
except Exception as erro:
    print(f'Causa do erro: {erro.__cause__}')
else:
    print(f'Resultado: {r}')
finally:
    print('FIM')
