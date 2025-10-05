class Pessoa:
    def __init__(self,alt,ida):
        self.altura = alt
        self.idade = ida
        print(f'A altura é {self.altura}m ',end='')
        print(f'e a idade é {self.idade} anos')

    def correr(self,no):
        self.nome = no
        print(f'{self.nome} está correndo')
    
    def comer(self,no):
        self.nome = no
        print(f'{self.nome} está comendo')

pessoa = Pessoa(1.75, 19)

pessoa.comer('Willians')