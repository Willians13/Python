veloc = float(input('Escreva a velocidade do carro : '))

if veloc > 80 :
    multa = (veloc - 80) * 7 
    print(' Velocidade acima do limite. Você foi multado, o valor que deverá pagar é : {}'.format(multa))
else:
    print(' Velocidade abaixo do limite ')