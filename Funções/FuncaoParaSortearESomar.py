from random import randint
lista = []
def sortear(lst):
    print('-' * 30)
    print(f'Os numeros sorteados foram: ',end=' ')
    for c in lst:
        print(c,end=' ')
    print(f'\n{"-" * 30}')

def somaPar(lst):
    soma = 0
    print('-' * 30)
    for num in lst:
        if num % 2 == 0:
            soma += num 
    print(f'A soma dos numeros pares é: {soma}')
    print('-' * 30)

for c in range(0,5):
    c += 1
    sorteio = randint(0,10)
    lista.append(sorteio)

sortear(lista)
somaPar(lista)
