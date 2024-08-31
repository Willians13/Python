
n =mult =0

while True :
    n = int(input('Quer ver a tabuada de qual valor (Numero negativo para encerrar): '))
    if n < 0:
        break
    cont = 0
    while cont < 10:
        cont += 1
        mult = n * cont
        print(f'{n} X {cont} = {mult}')    
print('FIM')