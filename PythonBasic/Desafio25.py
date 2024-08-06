sal = float(input(' Informe o seu salario : R$'))

if sal <= 1250:
    aumen = sal +(sal * (15/100))
    print('O seu salario teve um aumento de 15% e agora é {} '.format(aumen))
else:
    aumen = sal + (sal * (10 / 100))
    print('O seu salario teve um aumento de 10% e agora é {} '.format(aumen))


