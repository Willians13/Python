class Mamifero:
    def __init__(self,localizacao : str, nome: str) -> None:
        self.nome = nome
        self.localizacao = localizacao
    
    def andar(self) -> None:
        print(f'{self.nome} esta andando pelo: {self.localizacao}')
    
    

class Cachorro(Mamifero):
    def __init__(self, localizacao, nome, raca):
        super().__init__(localizacao, nome)
        self.raca = raca
    
    def latir(self)->None:
        print(f'{self.nome} da raça {self.raca} está latindo...')

class Gato(Mamifero):
    def __init__(self, localizacao, nome):
        super().__init__(localizacao, nome)

    def miar(self)->None:
        print(f'{self.nome} esta miando...')

dog1 = Cachorro('chile','Ares','Husky Siberiano')
dog1.andar()
dog1.latir()
print()
cat1 = Gato('Brasil','Lana')
cat1.andar()
cat1.miar()