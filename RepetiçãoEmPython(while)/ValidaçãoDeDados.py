sexo = str(input(' Informe seu sexo [M/F] : ').upper().strip())

while sexo not in 'MmFf':
    sexo = str(input(' Sexo invalido. Por favor, informe seu sexo corretamente : ').upper().strip())
    
print(' Sexo {} registrado com sucesso '.format(sexo))
