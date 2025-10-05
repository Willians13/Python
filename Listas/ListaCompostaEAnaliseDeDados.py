lista = []
total_pessoas =0
maior = menor = 0

while True:
    nome = (input('Digite o nome : '))
    peso = float(input('Digite o peso : '))
    total_pessoas += 1
    
    lista.append([nome, peso])
    
    r = (input('Quer continuar ? [S/N] ').upper().strip() [0])
    if r == 'N':
        break
    
    if total_pessoas == 1:
        maior = menor = peso 
    else:
        if peso > maior:
            maior = peso 
        if peso < menor:
            menor = peso

pessoa_maior_peso = []
pessoa_menor_peso = []

for i in lista:
    if i[1] == maior :
        pessoa_maior_peso.append(i[0])
        
for j in lista:
    if j[1] == menor:
        pessoa_menor_peso.append(j[0])
        
print(f'O maior peso foi {maior} Kg. Peso de {pessoa_maior_peso}')
print(f'O menor peso foi {menor} Kg. Peso de {pessoa_menor_peso}')
print(f'Foram cadastradas {total_pessoas} pessoas')