from random import randint
pc = 0
par = True
print(f'{"="*30}\nJOGO DO PAR OU IMPAR\n{"="*30}')
while True:
    pc = randint(0,20)
    n = int(input('Escolha um numero : '))
    esc=str(input('PAR OU IMPAR ? ').upper().strip()[0])
    if (n + pc) % 2 == 0:
        par = True
        print(f'Jogador escolheu {n} e o computador escolheu {pc}.Deu {n + pc} numero PAR')
    else:
        par = False
        print(f'Jogador escolheu {n} e o computador escolheu {pc}.Deu {n + pc} numero IMPAR')
    
    if esc == 'P' and par == True:
        print(f'Jogador venceu ')
    elif esc == 'P' and par == False:
        print(f'Jogador perdeu ')
        break
    elif esc == 'I' and par == True:
        print('Jogador perdeu')
        break
    elif esc == 'I' and par == False:
        print('Jogador venceu')
        
    