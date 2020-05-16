def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: um ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando a exibição ou não da situação a partir da média das notas
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)

    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


resp = notas(9, 10, 5.5, 2.5, 8.5)
print(resp)
