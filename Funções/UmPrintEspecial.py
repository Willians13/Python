def tamanhoTexto(txt):
    tamanho = len(txt) + 4
    print(f'{"~" * tamanho }')
    print(f'  {txt}')
    print(f'{"~" * tamanho }')
tamanhoTexto('Olá, mundo')
tamanhoTexto('Python') # Text