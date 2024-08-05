p = float(input('Informe o preço do produto : '))

desc = p - (p * (5 / 100))

print('O valor do produto é {} e com 5% de desconto fica {:.2f}.'.format(p, desc))