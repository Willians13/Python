numeros = [[],[]]
par = impar =0
for c in range(0,7):
    n = int(input(f'Digite o {c}º numero : '))
    numeros.append(n)
    if n % 2 == 0:
        par = n
        numeros[0].append(par)
    else:
        impar = n
        numeros[1].append(impar)

numeros[0].sort()
numeros[1].sort()
print(f'Lista dos pares {numeros[0]}')
print(f'Lista dos impares {numeros[1]}')
