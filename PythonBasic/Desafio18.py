nome = str(input(" Qual é o seu nome ? "))

print('Seu nome é : {}'.format(nome))
print('Seu nome em maiusculo : {}'.format(nome.upper()))
print('Seu nome em maiusculo : {}'.format(nome.lower()))
print('Seu nome tem : {} letra'.format(len(nome.replace(' ', '')))) 
print('Seu primeiro nome tem : {} letras '.format(len(nome.split()[0])))