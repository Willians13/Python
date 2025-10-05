lista = []
#Estrutura de repetição para adicionar os valores 
while True:
    
    valor = (input('Digite um numero : '))
    
#If para verificar se existe o valor na lista, se existir aparece uma mensagem de erro
    if valor in lista:
        print('Esse numero ja existe na lista ')
    else:
#Caso não exista adiona o valor a lista e mostra uma mensagem informando isso 
        lista.append(valor)
        print('Numero adicionado com sucesso...')
        
#Recebendo o valor de r, onde o usuario vai escolher se continua ou se para de adicionar numeros na lista 
    r = str(input('Quer continuar : [S/N]').upper().strip()[0])
    if r == 'N':
        break

#Mostrando a lista em ordem crescente 
print(f'{"=-" * 30}')
print(f'Sua lista : {sorted(lista)}')