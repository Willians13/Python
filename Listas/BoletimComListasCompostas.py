boletim = []
while True:
    nome =input('nome: ')
    nota1 =float(input('nota1: '))
    nota2 = float(input('nota2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2] , media])

    resp = (input('Quer continuar ? [S/N]').upper().strip()[0])
    if 'N' in resp:
        break

print(f'N.  Nome         Media')
print('--------------------------------')
for i, a in enumerate(boletim):
    print(f'{i:<3} {a[0]:<10} {a[2]:>5}')
while True:
    mostrar_nota = int(input('Mostrar notas de qual alunos ? (999 interrompe): '))
    if mostrar_nota == 999:
        print('Finalizando...')
        break
    if mostrar_nota <= len(boletim ) -1:
        print(f'Notas de {boletim[mostrar_nota][0]} são {boletim[mostrar_nota][1]}')