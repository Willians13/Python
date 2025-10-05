from datetime import datetime

def voto(nascimento):
    v = ' '
    ano_atual = datetime.now().year
    
    if ano_atual - nascimento >=18:
        v = 'Obrigatório'
        print(f'Com {ano_atual - nascimento} anos: O seu voto é {v}')
    elif ano_atual - nascimento == 16 or ano_atual - nascimento ==17:
        v ='Opcional'
        print(f'Com {ano_atual - nascimento} anos: O seu voto é {v}')
    elif ano_atual - nascimento < 16:
        v = 'Negado'
        print(f'Com {ano_atual - nascimento} anos: O seu voto é {v}')
        

nasc = int(input('Digite a data de nascimento: '))
voto(nasc)

