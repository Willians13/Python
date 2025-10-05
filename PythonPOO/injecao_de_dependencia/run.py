class Celular:
    def __init__(self, modelo: str) ->None:
        self.modelo = modelo
    
    def enviar_mensagem(self, mensagem) -> None:
        self.mensagem = mensagem 
        print(f'Enviando mensagem: {self.mensagem}')

    def abrir_emails(self) -> None:
        print('Abrindo emails...')
        
    def abrir_youtube(self) -> None:
        print('Abrindo o Youtube...')        
    

class Pessoa:
    def __init__(self,celular: Celular)->None:
        self.__celular = celular
    
    def pedir_pizza(self) ->None:
        print(f'Buscando o celular')
        print('Escolhendo o sabor...')
        self.__celular.enviar_mensagem('Quero uma de frango')
        print('Aguardando a chegada...')
    
    def estudar(self)->None:
        print('Sentando no computador')
        self.__celular.abrir_youtube()
        print('Estudando...')


android = Celular('Samsung')
iphone = Celular('iphone')

ana = Pessoa(android)
pedro = Pessoa(iphone)

ana.pedir_pizza()
print()
pedro.estudar()