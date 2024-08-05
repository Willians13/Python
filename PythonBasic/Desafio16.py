from random import choice

nome1 = str(input("Escolha um nome "))
nome2 = str(input("Escolha um nome "))
nome3 = str(input("Escolha um nome "))
nome4 = str(input("Escolha um nome "))

lista=[nome1,nome2,nome3,nome4]

sorteado = choice(lista)

print("O nome sorteado foi {}".format(sorteado))