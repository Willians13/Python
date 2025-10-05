from random import randint
maior = 0
menor = 0
for c in range(0,5):
    c += 1
    num = (randint(0,9))
    print(f'\nNumeros sorteados : {num}', end=' ')
    if c == 1:
        maior = 1
        menor = 1
    else:
        if num > maior:
            maior = num
        if menor > num:
            menor = num
print(f'\n{"-=" * 30}')
print(f'O maior numero é : {maior}')
print(f'O menor numero é : {menor}')
