casa = float(input('Qual o valor da casa ? R$ '))
salario = float(input('Qual o salário do comprador ? R$ '))
anos = int(input('Em quantos anos quer pagar a casa ? '))
prestacao = casa / (anos * 12)
minimo = salario * (30/100)

print('Para pagar uma casa de R${} em {} anos '.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print(' Emprestimo pode ser concedido ')
else:
    print(' Emprestimo NEGADO ')

