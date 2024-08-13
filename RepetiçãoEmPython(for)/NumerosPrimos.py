n = int(input(' Escreva um numero inteiro : '))

count = 0
count2 = 0

for c in range (1,n +1):
    if n % c == 0:
        print( '\033[33m', end = ' ')
        count = count + 1   
    else:
        print( '\033[31m', end = ' ')
    print('{}'.format(c), end='')
print('\n\033[m Numero {} foi divisivel {} vezes '.format(n, count))
if count == 2:
    print( ' É numero primo')
else:
    print(' Não é numero primo ')