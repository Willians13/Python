lista = []

#Estrutura de repetição para adicionar os valores 
while True :
    valor = int(input('Digite um valor : '))
    lista.append(valor)
    
#Recebendo o valor de r, onde o usuario vai escolher se continua ou se para de adicionar numeros na lista
    r = str(input('Quer continuar ? : [S/N]').upper().strip()[0])
    if 'N' in r :
        break
    
#Mostrando a quantidade de elementos na lista 
print(f'Quantidade de elementos na lista : {len(lista)}')

#Mostrando a lista de forma decrescente
print(f'A lista em forma decrescente : {sorted(lista, reverse=True)}')

#Criando uma condição para informar se existe numero 5 na lista 
if 5 in lista :
    print('5 faz parte da lista')
else:
    print('Não existe 5 na lista')