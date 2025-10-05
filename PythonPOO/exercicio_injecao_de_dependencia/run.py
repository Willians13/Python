class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.conection = None
        
    def conectar_banco(self) -> None:
        self.conection = True
    

class RepositorioDeBanco:
    def __init__(self,conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao
    
    def busca_dados(self) -> list:
        if self.__conexao.conection:
            return[1, 2, 3, 4, 5]
        
        return None

class RegraDeNegocio:
    def __init__(self,repo : RepositorioDeBanco):
        self.__repo = repo
    
    def calcular_resultados(self)->None:
        dados = self.__repo.busca_dados()
        if not dados:
            print('Dados não encontrados. Verifique sua conexão ao banco')
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f'O resultado é {resposta}')
        
    
conn = ConectorBancoDeDados()
conn.conectar_banco()

repo = RepositorioDeBanco(conn)
regra = RegraDeNegocio(repo)

regra.calcular_resultados()