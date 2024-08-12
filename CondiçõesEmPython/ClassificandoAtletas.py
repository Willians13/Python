from datetime import datetime

nasc = int(input(' Digite sua data de nascimento : '))

ano_atual = datetime.now().year

if ano_atual - nasc <= 9:
    print( ' Você tem {} anos, sua categoria é : Mirim '.format(ano_atual- nasc) )
elif ano_atual - nasc <= 14:
    print( ' Você tem {} anos, sua categoria é : Infantil '.format(ano_atual - nasc))
elif ano_atual - nasc <= 19:
    print( ' Você tem {} anos, sua categoria é : Junior '.format(ano_atual - nasc))
elif ano_atual - nasc <= 25:
    print( ' Você tem {} anos, sua categoria é : Senior '.format(ano_atual - nasc))
else:
    print( ' Você tem {} anos, sua categoria é : Master '.format(ano_atual - nasc))