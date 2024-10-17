class MinhaClasse:
    
    estatico = 'lhama'
    
    def __init__(self,estado) -> None:
        self.__estado = estado
        
    def print_variavel_de_classe(self) :
        print(self.estatico)
    
    @classmethod
    def alteracao_da_variavel_de_classe(cls):
        cls.estatico = 'Ola'
        # MinhaClasse.estatico = "ola"

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

obj1.print_variavel_de_classe()
obj1.alteracao_da_variavel_de_classe()

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)

