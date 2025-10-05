n1 = int (input(' Digite o primeiro valor inteiro : '))
n2 = int (input(' Digite o segundo valor inteiro : '))

opcao = 0

while opcao != 5:
    opcao = int(input('[1] - Soma\n[2] - Multiplicação\n[3] - Maior\n[4] - Novos Numeros\n[5] - Sair\n'))
    if opcao == 1:
        print('A soma entre {} e {} é : {} \n{}'.format(n1,n2, n1 + n2, '='*30))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é : {} \n{}'.format(n1,n2, n1*n2, '='*30))
    elif opcao == 3 :
        if n1 > n2:
            print('O maior numero entre {} e {} é : {}\n{}'.format(n1, n2, n1,'='*30))
        elif n1 < n2:
            print('O maior numero entre {} e {} é : {}\n{}'.format(n1, n2, n2,'='*30))
        else:
            print('Os dois numeros são iguais. Não existe maior')
    elif opcao == 4:
        n1 = int (input(' Digite o primeiro valor inteiro : '))
        n2 = int (input(' Digite o segundo valor inteiro : '))
print('Fim do programa ')

