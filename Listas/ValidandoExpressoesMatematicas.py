pilha = []
expre = str(input('Escreva uma expressão :'))
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão ta válida')
else:
    print('Sua expressão não é válida')
