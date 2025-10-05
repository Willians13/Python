maior = 0
auxiliar_media = 0 
count = 0

for c in range(1, 4+1):
    print( ' {} {}º PESSOA {}'.format('='*20, c , '='*20))
    nome = str(input( 'NOME : '))
    idade = int(input( 'IDADE : '))
    sexo = str(input( 'SEXO [M/F]: '.upper()))
    auxiliar_media = auxiliar_media + idade
    media = auxiliar_media / 4  
    if idade < 20:
        count = count + 1

if c == 1:
    maior = idade
else: 
    if idade > maior:
        maior = idade
        print('A maior idade é de {} que são {} anos '.format(nome, maior))
        
print('{} pessoas tem menos de 20 anos '.format(count))
print('A media de idade do grupo é {}'.format(media))



