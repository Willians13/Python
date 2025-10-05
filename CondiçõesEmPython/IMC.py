peso = float(input(' Informe seu peso em KG: '))
altura = float(input(' Informe sua altura em metros :'))

imc =  peso / (altura * altura) 
print(' Seu imc é {:.1f}'.format(imc))

if imc < 18.5:
    print(' Está abaixo do peso ')
elif imc < 25:
    print(' Peso ideal ')
elif imc < 30:
    print(' Sobrepeso ')
elif imc < 40:
    print(' Obesidade ')
else:
    print(' Obesidade mórbida')