n1 = float(input(" Digite o primeiro numero: "))
n2 = float(input(" Digite o segundo numero: "))

opcao = int(input(' Digite a opcao \n 1 - SOMA \n 2 - SUBTRAÇÃO \n 3 - DIVISAO \n 4 - MULTIPLICAÇÃO \n 5 - SAIR'))

if opcao == 1:
    print('RESULTADO: {} '.format (n1 + n2))
elif opcao == 2:
    print('RESULTADO: {}'.format (n1 - n2))
elif opcao == 3:
    print('RESULTADO: {}'.format(n1 / n2))
elif opcao == 4:
    print('RESULTADO: {}'.format (n1 * n2))
else:
    print('Saindo.....')
    