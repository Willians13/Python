class Mamifero:
    def __init__(self,localizacao : str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23
        
    def andar(self) -> None:
        print(f'O animal esta andando pelo: {self.localizacao}')
        
    def _dormir(self)->None:#Metodo Protegido
        print('O animal esta dormindo')
    
class Gato(Mamifero):
    def __init__(self, localizacao):
        super().__init__(localizacao)


    def miar(self)->None:
        print(f'O gato esta miando...')
        self._dormir()
        print(self._tamanho)
    
cat = Gato('Argentina')

cat.miar()
cat._dormir()#Deveria dar erro/ Elementos protegidos não são chamados por objetos
