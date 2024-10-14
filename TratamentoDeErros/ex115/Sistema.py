from lib import interface
from lib import arquivo
from time import sleep

arq = '__init__.py'

if arquivo.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')



while True: 
    resposta = interface.menu(['Ver Pessoa Cadastrada', 'Cadastrar Pessoas', 'Sair Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo...')
        break
    else:
        print(f'\033[31mErro! Digite uma opção valida!\033[0m')
    sleep(2)