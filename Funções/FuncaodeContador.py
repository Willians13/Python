from time import sleep

def contador(ini, fim, pas):
    if pas < 0 :
        pas *= -1
        
    if pas == 0:
        pas = 1
        
    print('-' * 30)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')

    if ini < fim:
        cont = ini 
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += pas
        print('FIM!')
    else:
        cont = ini 
        while cont >= fim:
            print(f'{cont}', end=' ',flush = True)
            sleep(0.5)
            cont -= pas
        print('FIM!')
    print('-' * 30)


#contador(0,100,10)
#contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)