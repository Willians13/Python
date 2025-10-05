from random import randint

jogador = int(input(' Escolha um numero inteiro entre 1 e 10 : '))

computador = randint(1,10)
erros = 0

while jogador != computador:
    jogador = int(input('ERROU. Tente novamente : ').strip())
    erros = erros + 1
    
print('O numero do jogador foi : {} \nO numero do computador é : {} \n{}'.format(jogador, computador, '=' *30))
print('Parabens, Acertou')
print('Jogador errou {} vezes ate acertar '.format(erros))