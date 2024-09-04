
numeros = ('zero', 'um', 'dois' , 'tres', 'quatro' , 'cinco' , 'seis', 'sete', 'oito', 
            'nove' , 'dez', 'onze' , 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
            'dezesete', 'dezoito', 'dezenovo', 'vinte')
while True:
    n = int(input('Escreva um numero entre 0 e 20 : '))  
    if n > 20 or n < 0 :
        print('Tente novamente', end = '.')
    else:    
        break
print(f'Você digitou o numero : {numeros[n]}') 