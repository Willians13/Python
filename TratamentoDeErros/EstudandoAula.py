try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite um numero:'))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dados que você informou!')
except (ZeroDivisionError):
    print('Não é possivel dividir um numero por 0!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados! ')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte Sempre!')