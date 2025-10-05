#Mostrando os 10 primeiros termos da progreção usando while

primeiro_termo = int(input('Informe o primero termo : '))
razao = int(input('Qual a razão : '))
c = 1

while c < 10:
    primeiro_termo = primeiro_termo + razao
    c = c + 1
    print('{} -> '.format(primeiro_termo),end= '')
print('FIM')