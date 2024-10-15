class Pessoa:
    def __init__(self,alt, cpf):
        self.altura = alt
        self.cpf = cpf
        
    def apresentar(self):
        print(f'Ola! minha altura - {self.altura}')
        self.__coletar_documento()
    
    def __coletar_documento(self): #Metodo Privado
        print(f'Meu documento - {self.cpf}')
    
jorge = Pessoa('1.94', '400.345.567-45')
ana = Pessoa('1.56', '098.765.432-11')

jorge.apresentar()