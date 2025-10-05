class Loja:
    taxa = 1.15
    def __init__(self,valor:float) -> None:
        self.valor_produto_bruto = valor
        

    def consultar_valor_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f'Valor do produto: {valor_produto:.2f}')

    @classmethod
    def editar_taxa_produto(cls,valor:float):
        cls.taxa = valor

loja_praia = Loja(30.50)
loja_shopping = Loja(10.39)

loja_praia.editar_taxa_produto(4.4)
loja_praia.consultar_valor_produto()
loja_shopping.consultar_valor_produto()