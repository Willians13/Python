nota1 = float(input(' Informe a sua primeira nota : '))
nota2 = float(input(' Informe a sua segunda nota : '))

media = (nota1 + nota2) / 2

if media < 5:
    print( 'Sua média é {}, está Reprovado '.format(media))
elif media >= 5 and media < 6.9:
    print( 'Sua média é {}, está em recuperação '.format(media))
elif media >= 7 and media <=10:
    print( 'Sua média é {}, está Aprovado '.format(media))
else :
    print( ' Notas erradas ')
