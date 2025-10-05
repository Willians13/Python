lista = []
mulheres = []
pessoa = {}
total = media = mulher =0
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo:[M/F]').strip().upper()[0]
    
    if pessoa['sexo'] not in ['M', 'F']:
        pessoa['sexo'] = input('ERRO! Tente Novamente: ').strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
        
    pessoa['idade'] = int(input('Idade: '))
    
    lista.append(pessoa.copy())
    total+=1
    
    res = input('Quer continuar ? [S/N]').strip().upper()[0]
    if 'N' in res:  
        break
    
soma_idade = 0
for p in (lista):
    soma_idade += p['idade']
media = soma_idade / total


print(f'{"=" * 50}')
print(f'O numero total do grupo é: {total}')
print(f'A media de idade do grupo é: {media:.2f} anos')
print(f'As mulheres do grupo são: {mulheres}')
print('Pessoas com a idade acima da media : ')
for p in (lista):
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v};',end =' ')
        print()