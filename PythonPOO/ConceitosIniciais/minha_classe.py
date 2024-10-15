class MinhaClasse:
    def __init__ (self, info, elem): # Metodo Construtor! Sempre é o primeiro à executar
        self.atributo_1 = 'meu atributo 1'
        self.atributo_2 = [1, 2, 'a']
        self.atributo_3 = elem
        self.atributo_novo = info
        print(self.atributo_novo)
        print(self.atributo_3)

    def metodo_1(self):
        print('Minha ação 1')
        print('Minha ação 2')
        print(self.atributo_2)
        return 'Ola, Mundo'
    
    def metodo_2(self,numero):
        self.metodo_1()
        print(f'A soma de {self.atributo_2[1]} + {numero} é {self.atributo_2[1] + numero}')

#Objeto        Classe ->    Instanciando um Objeto
minha_classe =MinhaClasse('Info aqui no construtor ', 123)

minha_classe.metodo_2(5)

#response = minha_classe.metodo_1()
#print(response)