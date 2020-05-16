frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece: {} vezes'.format(frase.upper().count('A')))
print('A primeira posição da letra A foi: {}'.format(frase.upper().find('A') + 1))
print('A ultima posição da letra A foi: {}'.format(frase.upper().rfind('A')+1))
