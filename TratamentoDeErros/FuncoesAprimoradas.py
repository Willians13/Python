def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
            return n
        except ValueError:
            print('ERRO! Digite um numero inteiro valido')
        except KeyboardInterrupt:
            print('\nO usuario preferiu não informar os dados! ')
            return 0

def leiafloat(txt):
    while True:
        try:
            n2=float(input(txt))
            return n2
        except ValueError:
            print('ERRO! Digite um numero real valido')
        except KeyboardInterrupt:
            print('\nO usuario preferiu não informar os dados! ')
            return 0
            
n = leiaInt('Digite um numero Inteiro: ')
n2= leiafloat('Digite um nuemro Real: ')
print(f'Você digitou o numero inteiro {n} e o real {n2}')