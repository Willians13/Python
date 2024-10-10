from time import sleep

def maior(*num):
    print(f'{"-"* 50} ')
    print('Numeros informados:',end='')
    for s in num:
        sleep(1)
        print(f'{s}',end=' ', flush =True)
    print(f'foram informados {len(num)} numeros.\nO maior numero é : {max(num)}')
    
maior(4,5,1,9)
maior(7,5)
maior(9,0,3,5,1,6)
maior(8)

