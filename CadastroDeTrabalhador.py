from datetime import datetime
cadastro = {}
ano_atual = datetime.now().year

cadastro['nome'] = input('Nome: ')
data_nascimento = int(input('Data de nascimento: '))
cadastro['nascimento'] = ano_atual - data_nascimento

cadastro['CTPS'] = int(input('Numero da carteira de trabalho: (0 se não tem)'))

if cadastro['CTPS'] == 0:
    cadastro['CTPS'] = 0
    print(f'{"=" * 50}')
    print(cadastro)
    print(f' O nome tem valor : {cadastro["nome"]}\n A idade tem valor: {cadastro["nascimento"]}'
        f'\n CTPS tem valor: {cadastro["CTPS"]}')
else:
    cadastro['contrato'] = int(input('Ano de contrato: '))
    cadastro['salario'] = float(input('Salario: R$'))
    cadastro['aposentadoria'] = cadastro['nascimento']+((cadastro['contrato'] + 35) - ano_atual)
    print(f'{"=" * 50}')
    print(cadastro)
    print(f' O nome tem valor : {cadastro["nome"]}\n A idade tem valor: {cadastro["nascimento"]}'
    f'\n CTPS tem valor: {cadastro["CTPS"]}\n Contratação tem o valor: {cadastro["contrato"]}'
    f'\n Salario : {cadastro["salario"]}R$\n Aposentadoria: {cadastro["aposentadoria"]}')
    


    