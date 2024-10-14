def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n=input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero inteiro valido')
        if ok:
            break
    return valor
    
n = leiaInt('Digite um numero: ')
print(f'Você digitou o numero {n}')