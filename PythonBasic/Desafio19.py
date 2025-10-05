import random
num = int(input('Escolha um numero de 1 à 5: '))

escolhido = random.randint(1,5)

if num == escolhido:
    print(' Parabens você acertou ')
else:
    print(' Você errou ')