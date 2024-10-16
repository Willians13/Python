class SistemaCadastral:
    
    def cadastrar(self, nome:str, idade : int) -> None:
        if self.__validate_input(nome,idade):
            self.__register_user(nome,idade)
        else:
            self.__error()
            
    def __validate_input(self, nome:str, idade:int) -> bool:
        return isinstance(nome,str) and isinstance(idade,int)

    def __register_user(self, nome:str, idade:int) -> None:
        print('Acessando o Banco de Dados....')
        print(f'Cadastrar Usuario {nome}, idade {idade}')
    
    def __error(self) -> None:
        print('Dados invalidos ')
    
pessoa1 = SistemaCadastral()
pessoa1.cadastrar('Willians', 19)