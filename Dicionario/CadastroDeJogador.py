jogador = {}
gols = []
total_gols = 0

jogador['nome'] = input('Nome: ')
jogador['partidas'] = int(input(f'{jogador["nome"]} jogou quantas partidas ?'))

for c in range(jogador['partidas']):
    gols.append( int(input(f'Quantos gols na {c+1}º partida ? ')))
    jogador['rendimento'] = gols
    total_gols = sum(gols)
    
print(f'{"=" * 50}')
print(jogador)
print(f'{"=" * 50}')
print(f'Nome: {jogador["nome"]}\nQuantidade de partidas: {jogador["partidas"]}'
    f'\nGols:{jogador["rendimento"]}\nTotal de gols: {total_gols}')
print(f'{"=" * 50}')

for k, v in enumerate(jogador["rendimento"]):
    print(f'Na partida {k+1} fez {v}')
print(f'Total de gols: {total_gols}')