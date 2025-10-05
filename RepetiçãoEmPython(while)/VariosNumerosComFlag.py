count = soma= 0
while True:
    n = int(input('Escreva um numero [DIGITE 999 PARA PARAR]: '))
    if n == 999:
        break
    count+=1
    soma += n
print(f'O total de numeros é {count} e a soma entre eles é {soma}')
    