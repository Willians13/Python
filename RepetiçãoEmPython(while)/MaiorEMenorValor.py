resp = 'S'
soma = quant = media = 0

while resp in 'Ss':
    num = int(input(' Escreva um numero : '))
    soma += num
    quant+= 1
    if quant == 1:
        maior = num 
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor :
            menor = num
    resp = str(input('Quer continuar ? [S/N] :')).upper().strip()[0]
media = soma / quant
print('O maior numero é o {} e o menor é o {}'.format(maior, menor))
print('Voce digitou {} numeros e a media é {}'.format(quant, media))