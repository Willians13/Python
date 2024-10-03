lista = []

while True:
    jogador = {}
    gols = []
    
    jogador['nome'] = input('Nome: ')
    jogador['partidas'] = int(input(f'{jogador["nome"]} jogou quantas partidas? '))

    for c in range(jogador['partidas']):
        gol = int(input(f'Quantos gols na {c+1}ª partida? '))
        gols.append(gol)
    
    jogador['rendimento'] = gols
    jogador['total'] = sum(gols)  
    lista.append(jogador.copy())
    
    res = input('Quer continuar? [S/N] ').strip().upper()[0]
    if res == 'N':
        break

print(f'{"=" * 50}')


print(f'{"No":<6} {"Nome":<15} {"Gols":<20} {"Total de Gols":<15}')
print('-' * 50)
for i, jogador in enumerate(lista):
    print(f'{i:<6} {jogador["nome"]:<15} {str(jogador["rendimento"]):<20} {jogador["total"]:<15}')

print('-' * 50)
