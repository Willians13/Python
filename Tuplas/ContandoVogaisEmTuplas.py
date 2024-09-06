palavras = ('Nebulos', 'Cacto', 'Serenidade', 'Fragmento', 'Eclipse')
for p in palavras:
    print(f'\nNa palavra {p} temos: ',end ='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}',end=', ')