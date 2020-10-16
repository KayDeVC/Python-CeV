def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: um valor opicional, indicando se deseja ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif 5 <= r['média'] < 7:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(7.5, 6.5, 9.5, 7.5, sit=True)
print(resp)
help(notas)
