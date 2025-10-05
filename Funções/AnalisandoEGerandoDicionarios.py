def notas(*n, sit = False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] > 7 :
            r['situacao'] = 'Boa'
        elif r['media'] >=5:
            r['situacao'] = 'Razoavel'
        else:
            r['situacao'] = 'Ruim'
    return r

resp = notas(5.5, 6, 7.1,1, sit=True)
print(resp)