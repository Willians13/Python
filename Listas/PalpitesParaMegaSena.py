from random import randint

lista = []
jogos = []
cont = 0
quantidade = int(input('Quantas listas quer ?'))
tot = 0

while tot < quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:]) 
    lista.clear()  
    tot += 1

print(f'{"-=" *3} Sorteando {"-=" *3}')

for i , l in enumerate(jogos):
    print(f'Jogo {i} : {l}')



    