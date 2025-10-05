km = float(input('Informe a quantidade de km percorridos : '))
dia = int(input('Informe a quantidade de dias que ficou com o carro : '))

rodado = km * 0.15
totdias = dia * 60

total = rodado + totdias

print('O valor total que deve pagar é {}'.format(total))