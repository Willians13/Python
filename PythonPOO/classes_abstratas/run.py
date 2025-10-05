from abc import ABC, abstractmethod

class Pessoa(ABC): #Classe abstrata não possui objetos - só pode ser mãe(Herança)
    def correr(self):
        print('A pessoa esta correndo de manhã ')
    
    @abstractmethod # A classe filha DEVE criar um metodo trabalhar
    def trabalhar(self):
        pass
    
class Professor(Pessoa):
    def trabalhar(self):
        print('O professor esta dando aula')

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print('O cozinherio esta cozinhando')



p1 = Professor()
p1.trabalhar()
p1.correr()

print()

p2 = Cozinheiro()
p2.trabalhar()
p2.correr()
