def notas(*notas, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    dicionario['total'] = len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)
    dicionario['média'] = sum(notas)/len(notas)
    if sit:
        if dicionario['média'] >= 7:
            dicionario['situação'] = 'BOA'
        elif dicionario['média'] >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
