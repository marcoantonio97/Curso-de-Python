from random import choice
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
sorteio = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi {}'.format(choice(sorteio)))
