def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

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
        
def menu(lista):
    cabeçalho('Menu Principal')
    c = 0
    for i in lista:
        c+=1
        print(f'{c} - {i}')
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc


