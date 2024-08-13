s = 0
count = 0
for c in range(0, 6):
    n = int(input(' Escreva um numero : '))
    if n % 2 ==0 :
        s = s + n
        count = count + 1
print('Você informou {} numeros PARES e a soma foi {}'.format(count, s))