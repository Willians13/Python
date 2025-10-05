class MinhaClasse:
    def __init__(self):
        self.__valor = None
        self._elemento = None
        
    def setter_elemento(self, elemento : str):
        self.__elemento = elemento
    
    def getter_elemento(self) -> str:
        return self.__elemento
        
    def setter_valor(self, valor:int) -> None: 
        self.__valor = valor

    def getter_valor(self) -> int:
        return self.__valor


my_class = MinhaClasse()

my_class.setter_elemento('Tudo bem? ')
elemento = my_class.getter_elemento()
print(elemento)

my_class.setter_valor(4)
valor = my_class.getter_valor()
print(valor)