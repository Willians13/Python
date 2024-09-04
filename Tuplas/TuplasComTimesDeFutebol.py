tabela = 'Botafogo', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense', 'Athletico-PR', 'Internacional', 'Cruzeiro', 'São Paulo', 'Red Bull Bragantino', 'Fortaleza', 'Atlético-MG', 'Corinthians', 'Vasco', 'Goiás', 'Bahia', 'Santos', 'Coritiba', 'Cuiabá', 'América-MG'
print(f'{"-=" *40}')
print(f'Tabela campeonato brasileiro : {sorted(tabela)}')
print(f'{"-=" * 40}')
print(f'Primeiros 5 colocados{tabela [0:5]}')
print(f'{"-=" * 40}')
print(f'Ultimos 4 colocados : {tabela[16:20]}')
print(f'{"-=" * 40}')
print(f'O {tabela[7]} está na {tabela.index("Cruzeiro")}º posição')