import moeda


p = float(input('Digite o preço: R$'))

print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'Aumentado: {moeda.aumentar(p, 10)}')
print(f'Diminuindo: {moeda.diminuir(p, 13)}')