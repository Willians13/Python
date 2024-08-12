frase = 'Curso em Video Python'

#print(frase[9]) Mostra a letra
#print(frase[9:14])Mostra da letra nove ate a 13
#print(frase[9:21:2]) Mostra pulando de 2 em 2
#print(frase[:5])Mostra do inicio ate o numero informado
#print(frase[9::3]) Mostra do nove ate o fim de 3 em 3

print(len(frase))#Mostra a quantidade de letras na frase
print(frase.count('o'))#Mostra a quantidade de 'o' na frase
print(frase.count('o',0,13))#Mostra a quantidade de 'o' na frase d 0 ate 12
print(frase.find('deo'))#Mostra a posição do 'deo'
print(frase.find('android'))#Se n existir a palavra mostra o resultado -1
print('Curso' in frase)
print(frase.replace('Python', 'Android'))#Substitui 
print(frase.upper())#Frase em maiusculo
print(frase.lower())#Frase minusculo
print(frase.capitalize())#Apenas a primeira letra da frase em maiusculo
print(frase.title())#Todas as iniciais de palavras ficam maiusculas
print(frase.split())#divide uma string em uma lista
print('-'.join(frase))



"""
frase2 = '   Aprenda Python  '

print(frase2.strip())#Tira os espaços do inicio e do fim da frase
print(frase2.rstrip())#Tira os espaços do fim (lado direito)
print(frase2.lstrip())#Tira os espaços do inicio (lado esquerdo)
"""