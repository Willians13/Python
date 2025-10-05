#Mostrando inicialmente 10 primeiros termos da progreção usando while e dando a opção de mostrar mais termos

primeiro_termo = int(input('Informe o primero termo : '))
razao = int(input('Qual a razão : '))
c = 1
total = 0
mais = 10
while mais != 0 :
    total = total + mais
    while c < total:
        primeiro_termo = primeiro_termo + razao
        c = c + 1
        print('{} -> '.format(primeiro_termo),end= '')
    print('PAUSA')
    mais = int(input('Quantos termos vc quer mostrar a mais ? '))
print('No total teve {} numeros'.format(total))
print('FIM')
