lista= []
par = soma_par = 0
for c in range(0,9):
    n = int(input('Digite um valor : '))
    lista.append(n)
    if n % 2 ==0:
        par = n
        soma_par += par
        
soma_terceiraCol = lista[2] + lista[5] + lista[8]
        
print(f'[{lista[0]:^5}] [{lista[1]:^5}] [{lista[2]:^5}]')
print(f'[{lista[3]:^5}] [{lista[4]:^5}] [{lista[5]:^5}]')
print(f'[{lista[6]:^5}] [{lista[7]:^5}] [{lista[8]:^5}]')

print(f'A soma de todos os numeros pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_terceiraCol}')

if lista[0] > lista[1] and lista[0] > lista[2]:
        print(f'O maior valor da segunda linha é {lista[0]}')
elif lista[1] > lista[0] and lista[1] > lista[2]:
        print(f'O maior valor da segunda linha é {lista[4]}')
elif lista[2] > lista[1] and lista[2] > lista[0]:
        print(f'O maior valor da segunda linha é {lista[7]}')