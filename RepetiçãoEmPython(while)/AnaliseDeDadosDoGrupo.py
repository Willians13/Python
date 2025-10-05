count_idade = count_homem =count_mulher= 0
while True:
    print(f'{"=" * 30}\nCADASTRE UMA PESSOA\n{"="*30}')
    
    idade = int(input('Idade : '))   
    sexo = str(input('Sexo [M/F] : ').upper().strip()[0])
    while sexo not in ['M','F']:
        sexo = str(input('Sexo [M/F] : ').upper().strip()[0])
        
    if sexo in 'M':
        count_homem += 1
        
    if idade > 18:
        count_idade += 1
        
    if idade > 20 and sexo in 'F':
        count_mulher += 1
        
    continuar = str(input('Quer continuar ?[S/N]').upper().strip()[0])
    while continuar not in ['S','N']:
        continuar = str(input('Quer continuar ?[S/N]').upper().strip()[0])
    if continuar in 'Nn':
        break
    
print(f'Total de pessoas com mais de 18 anos : {count_idade} ')
print(f'Numero de homens cadastrados : {count_homem}')
print(f'Numero de mulheres maiores de 20 anos : {count_mulher}')


