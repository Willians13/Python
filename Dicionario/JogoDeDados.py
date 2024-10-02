from random import randint

dado = {} 

for c in range(0,4):
    dado['jogada'] = randint(1,6)
    c+=1
    dado['jogador'] = c
    print(f'O jogador {dado["jogador"]} tirou {dado["jogada"]}')

    