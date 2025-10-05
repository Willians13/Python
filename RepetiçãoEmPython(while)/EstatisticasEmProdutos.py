count_preco =count_mil= barato = 0
while True:
    nome_pro = str(input('Escreva o nome do produto : '))
    preco_prod = float(input('Qual o valor do produto ? R$'))
    count_preco += preco_prod
    
    if preco_prod > 1000:
        count_mil += 1
        
    continuar = str(input('Quer continuar ? [S/N]').upper().strip()[0])
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar ? [S/N]').upper().strip()[0])
        
    barato = preco_prod
    if preco_prod < barato:
        barato = preco_prod
        
    if continuar in 'N':
        break   
    
print(f'O preço total da compra deu : {count_preco}')
print(f'A quantidade de produtos acima de 1000 reias é : {count_mil}')
print(f'O produto com o preço mais barato é : {barato}')