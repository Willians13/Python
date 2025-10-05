preco =float(input(' Informe o valor da compra : R$ '))
opcao =int(input(''' Formas de pagamento \n 1 - à vista dinheiro/cheque \n 2 - á vista cartão \n 3 - 2x no cartão \n 4 - 3x ou mais no cartão '''))


if opcao == 1:
    total =preco -(preco * (10/100))
    print(' Você teve 10% de desconto e o valor final ficou {}'.format(total))
elif opcao == 2:
    total =preco -(preco * (5/100))
    print(' Você teve 5% de desconto e o valor final ficou {}'.format(total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2X de {} ' .format(parcela))
elif opcao == 4:
    total = preco + (preco * (20/100))
    totparc = int(input(' Quantas parcelas ?'))
    parcela = total / totparc
    print(' Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else: 
    total = preco
    print(' Opção invalida ')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final '.format(preco, total))

