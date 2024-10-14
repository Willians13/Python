def ficha(nome ='<Desconhecido>', gols=0):
    if nome =='':
        nome = '<Desconhecido>' 
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols')
    
n = input('Escreva o nome do jogador: ')
g = input('Quantos gols ele fez? ')

ficha(n,g)