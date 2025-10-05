class SistemaCadastral:
    
    def __init__(self, nome:str, idade : int) -> None:
        if isinstance(nome,str) and isinstance(idade,int):
            print('Acessando o Banco de Dados....')
            print(f'Cadastrar Usuario {nome}, idade {idade}')
        else:
            print('Dados invalidos ')
        