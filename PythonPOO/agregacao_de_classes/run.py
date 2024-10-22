class Produto:
    def __init__(self,prod_nome:str, prod_valor:float)->None:
        self.__prod_nome = prod_nome
        self.__prod_valor = prod_valor
    
    def informacoes_produtos(self):
        print(f'O {self.__prod_nome} custa: R${self.__prod_valor:.2f}')
    
class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []
    
    def adicionar_produto(self,produto: type[Produto]) ->None:
        self.__produtos.append(produto)
    
    def finalizar_compra(self)-> None:
        print(f'Compras finalizadas!')
        
        for produto in self.__produtos:
            produto.informacoes_produtos()

car = CarrinhoDeCompras()
monitor = Produto('Monitor', 150.99)
car.adicionar_produto(monitor)

mouse = Produto('Mouse', 50)
car.adicionar_produto(mouse)

teclado = Produto('Teclado', 78.50)
car.adicionar_produto(teclado)

car.finalizar_compra()

        
        