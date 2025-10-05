pt = int(input(' Primeiro termo: '))
r = int(input( ' Razão: '))
dec = pt + (11 - 1) * r

for c in range(pt, dec, r):
    print('{} '.format(c),end='-> ')
    
print(' Acabou ')