from datetime import datetime

nasc = int(input(' Em que ano nasceu ?'))

ano_atual = datetime.now().year

if ano_atual - nasc < 18:
    print(' Só tem {} anos '.format(ano_atual - nasc))
    print('Ainda faltam mais {} anos'.format(18 -(ano_atual - nasc)))
elif ano_atual - nasc == 18:
    print(' Ja tem {} anos, pode se alistar'.format(ano_atual - nasc))
else:
    print(' Ja tem {} anos, passou do tempo de se alistar'.format(ano_atual - nasc))