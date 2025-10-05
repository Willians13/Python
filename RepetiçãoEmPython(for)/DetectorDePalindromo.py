frase = str(input(' Escreva uma frase : ').replace(' ', '').upper())
frase_inversa = frase[::-1]

if frase == frase_inversa:
    print('=' * 30)
    print('{} ao contrario é {}'.format(frase, frase_inversa).upper())
    print(' A frase digitada é um Palíndromo')
    print('=' * 30)
else:
    print('=' * 30)
    print('{} ao contrario é {}'.format(frase, frase_inversa))
    print(' A frase digitada não é um palíndromo ' ) 
    print('=' * 30)
