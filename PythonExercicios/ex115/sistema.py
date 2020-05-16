from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


cabecalho('SISTEMA ARQUIVO')
while True:
    resp = menu(['Listar Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('3- Sair do Sistema')
        break
    else:
        print('ERRO! Digite uma opção válida: ')
    sleep(2)
