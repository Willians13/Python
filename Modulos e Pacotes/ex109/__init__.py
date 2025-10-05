import moeda
p = float(input('Digite o preço: R$'))

print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'Aumentando: {moeda.aumentar(p,10,True)}')
print(f'Diminuindo: {moeda.diminuir(p,13,True)}')