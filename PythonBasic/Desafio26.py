l1 = float(input(' Escreva o valor do primeiro lado : '))
l2 = float(input(' Escreva o valor do segundo lado : '))
l3 = float(input(' Escreva o valor do terceira lado : '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(' É possivel formar um triangulo ')
else:
    print(' Não é possivel formar um triangulo ')