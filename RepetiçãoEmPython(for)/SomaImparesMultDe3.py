i = 0
count = 0
for c in range(1,500+1, 2):
    if c % 3 == 0 :
        count = count + 1
        i = i + c
print('O resultado de todos os {} numeros somados é {}'.format(count, i))