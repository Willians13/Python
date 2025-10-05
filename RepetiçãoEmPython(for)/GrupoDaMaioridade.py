from datetime import datetime

ano_atual = datetime.now().year
count = 0
count2 = 0

for c in range(1, 8):
    ano = int(input( ' Em que ano a {}º pessoa nasceu : '.format(c)))  
    if ano_atual - ano >= 21:   
        count = count + 1
    else :
        count2 = count2 + 1
    

print(' {} pessoas atingiram a maioridade '.format(count))
print( ' {} pessoas não atingiram a maioridade'.format(count2))