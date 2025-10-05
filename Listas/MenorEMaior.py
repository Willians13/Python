lista = []

for c in range(0,5):
#Adicionando valores na lista
    valor = int(input(f'Escreva o valor da posição {c}: '))
    lista.append(valor)
    
#Criando duas variaveis para o maior e o menor numero
maior_num = max(lista)
menor_num = min(lista)

#Usando o enumerate para saber o valor e o indice 
print(f'O maior numero : {maior_num}. Na posição : ',end='')
for i, v in enumerate(lista):
    if v == maior_num:
        print(f'{i}... ',end='')

print(f'\nO menor numero : {menor_num}. Na posição : ',end='')
for i, v in enumerate(lista):
    if v == menor_num:
        print(f'{i}...',end='')
    


