def dobro(n,form=False):
    dob = n* 2
    return dob if form is False else moeda(dob)

def metade(n,form=False):
    met = n /2
    return met if form is False else moeda(met)

def aumentar(n,p,form=False):
    aum = n + (n *(p/ 100))
    return aum if form is False else moeda(aum)

def diminuir(n, p,form=False):
    dim = n - (n *(p/ 100))
    return dim if form is False else moeda(dim)

def moeda(n):
    numero = str(n)
    texto = 'R$'
    junto = texto + numero
    return junto

def resumo(n,p,d):
    print('-' * 40)
    print(f'{"Resumo do Valor":^40}')
    print('-' * 40)
    print(f'Preço analisado {n}')
    print(f'O dobro de {n} é {dobro(n)}')
    print(f'A metade de {n} é {metade(n)}')
    print(f'Aumentado: {aumentar(n,p)}')
    print(f'Diminuindo: {diminuir(n,d)}')