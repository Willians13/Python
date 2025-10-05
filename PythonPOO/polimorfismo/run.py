class ClasseQualquer:
    def fazer(self) -> None:
        print('Estou fazendo algo...')

class OutraCoisa:
    def preparar(self) -> None:
        print('Estou preparando algo...')
    
    def fazer(self) -> None:
        print('Estou fazendo outra coisa...')
    


obj1 = ClasseQualquer()
obj2 = OutraCoisa()

#Dois metodos iguais que fazem coisas diferentes
obj1.fazer()
obj2.fazer()