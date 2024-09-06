produtos = ('lapis', 3.56, 'borracha', 2.45, 'caderno', 12.99, 'caneta', 4.25, 'régua', 5.60, 'marca-texto', 7.30)

print(f'{"-" * 40}')
print(f'{"Listagem de produtos":^40}')
print(f'{"-" * 40}')
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}',end='R$ ')
    else:
        print(f'{produtos[c]}')