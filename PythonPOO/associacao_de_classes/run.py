class Interruptor:
    def __init__(self, comodo:str) -> None:
        self.comodo = comodo
    
    def acender(self) -> None:
        print(f'Luzes do comodo {self.comodo} estão ligadas ')

    def apagar(self) -> None:
        print(f'Luzes do comodo {self.comodo} estão desligadas ')
    
class Pessoa:
    def acender_luzes(self, interruptor: Interruptor) -> None:
        interruptor.acender()
        
    def apagar_luzes(self, interruptor: Interruptor) -> None:
        interruptor.apagar()
        
    def dormir(self):
        print('Indo dormir...')

ana = Pessoa()
interruptor_quarto = Interruptor('quarto')
interruptor_sala = Interruptor('sala')

ana.acender_luzes(interruptor_sala)
ana.apagar_luzes(interruptor_quarto)
ana.dormir()


        