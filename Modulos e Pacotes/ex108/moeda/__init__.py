def dobro(n):
    return n * 2

def metade(n):
    return n / 2

def aumentar(n,p):
    aux = n + (n *(p/ 100))
    return aux

def diminuir(n, p):
    aux = n - (n *(p/ 100))
    return aux

def moeda(n):
    numero = str(n)
    texto = 'R$'
    junto = texto + numero
    return junto