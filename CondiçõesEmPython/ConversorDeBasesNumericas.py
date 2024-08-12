n = int(input(' Informe um valor inteiro : '))

print( 'Em que base numerica quer converter esse numero : ')
opcao = int (input( ' 1 - Binário\n 2 - Octal \n 3 - Hexadecimal \n 4 - sair \n'))

if opcao == 1:
    print('{} em BINÁRIO é : {}'.format(n,bin(n)[2:]))
elif opcao == 2:
    print('{} em OCTAL é : {}'.format(n,oct(n)[2:]))
elif opcao == 3:
    print('{} em HEXADECIMAL é : {}'.format(n,hex(n)[2:]))
elif opcao == 4:
    print(' Saindo....')
else:
    print('Opção errada')
