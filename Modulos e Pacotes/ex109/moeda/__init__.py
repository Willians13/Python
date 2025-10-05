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