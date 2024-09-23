lista1 = []
lista_Par = []
lista_Impar = []

#Estrutura de repetição para adicionar os valores 
while True :
    valor = int(input('Digite um valor : '))
    lista1.append(valor)
    
#Verificando se o numero é par ou impar 
    if valor % 2 == 0:
        lista_Par.append(valor)
    else:
        lista_Impar.append(valor)
    
#Recebendo o valor de r, onde o usuario vai escolher se continua ou se para de adicionar numeros na lista
    r = str(input('Quer continuar ? : [S/N]').upper().strip()[0])
    if 'N' in r :
        break

#Mostrando a lista completa, a lista par e a lista impar em ordem crescente
print(f'Sua lista : {sorted(lista1)}')
print(f'Lista apenas com os numeros pares : {sorted(lista_Par)}')
print(f'Lista apenas com os numeros impares : {sorted(lista_Impar)}')