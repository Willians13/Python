class MinhaClasse:
    
    estatico = 'lhama'
    
    def __init__(self,estado) -> None:
        self.__estado = estado
        

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estetico = 'programador'
obj1.estatico = 'Ola, Mundo'
MinhaClasse.estatico = 'LhamaAqui'

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)