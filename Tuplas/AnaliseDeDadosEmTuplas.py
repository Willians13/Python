
num =(int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')))
print(f'A quantidade de 9 é {num.count(9)}')
if 3 in num :
    print(f'O primeiro numero 3 aparece na  {num.index(3)+1}º posição')
else:
    print('Não existe numero 3 na tupla')
    
print('Os numeros pares são : ',end= '')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')