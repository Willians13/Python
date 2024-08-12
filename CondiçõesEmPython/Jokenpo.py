import random

print('=' * 30)
opcao = int(input(' Escolha uma opcao :\n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n 4 - Sair \n {} \n'.format('=' * 30) ))


jogada = ['Pedra', 'Papel', 'Tesoura']
maquina = random.choice(jogada)

if opcao == 1:
    opcao = 'Pedra'
    print('Jogador escolheu : {}'.format(opcao))
    print('Maquina escolheu : {}'.format(maquina))
    print('{} \nResultado :'.format('=' * 30))
elif opcao == 2:
    opcao = 'Papel'
    print('Jogador escolheu : {}'.format(opcao))
    print('Maquina escolheu : {}'.format(maquina))
    print('{} \nResultado :'.format('=' * 30))
elif opcao == 3:
    opcao = 'Tesoura'
    print('Jogador escolheu : {}'.format(opcao))
    print('Maquina escolheu : {}'.format(maquina))
    print('{} \nResultado :'.format('=' * 30))
elif opcao == 4:
    print(' Saindo....... ')
else:
    print(' Opção errada ')


if opcao == 'Pedra' and maquina == 'Pedra' or opcao == 'Papel' and maquina == 'Papel' or opcao == 'Tesoura' and maquina == 'Tesoura':
    print('Empate')
elif opcao == 'Pedra' and maquina == 'Tesoura' or opcao == 'Papel' and maquina == 'Pedra' or opcao == 'Tesoura' and maquina == 'Papel':
    print('Jogador Ganhou')
elif maquina == 'Pedra' and opcao == 'Tesoura' or maquina == 'Papel' and opcao == 'Pedra' or maquina == 'Tesoura' and opcao == 'Papel':
    print('Maquina Ganhou')




