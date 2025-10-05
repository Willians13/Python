import urllib.request
import ssl

context = ssl._create_unverified_context()

try:
    site = urllib.request.urlopen('https://www.pudim.com.br', context=context)
except Exception as e:
    print(f'Deu erro: {e}')
else:
    print('Site Acessível')