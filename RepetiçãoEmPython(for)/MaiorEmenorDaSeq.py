maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input( ' Informe o peso da {} pessoa : '.format( c )))
    if c == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso    
print('O maior peso é {} KG'.format(maior))
print('O menor peso é {} KG'.format(menor))