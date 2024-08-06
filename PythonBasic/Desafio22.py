dist = float(input(' Escreva a distancia da sua viagem em KM : '))

if dist <= 200:
    valor = dist * 0.50
    print(' O valor da viagem é : {}'.format(valor))
else:
    valor = dist * 0.45
    print(' O valor da viagem é : {}'.format(valor))