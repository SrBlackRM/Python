import requests  #Beautiful Soup 4 / BS4
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/results?search_query='
print('Digite o que quer pesquisar no Youtube: ')
pesquisa = str(input())
parm = '&pbj=1'

url_pesquisa = url+pesquisa+parm

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com',
             'cf-ipcountry': 'US'}
meus_cookies = {'Ultima-visita':'10-10-2020'}

dados = {'username': 'mota',
         'senha': '12345'}

try:
    r = requests.get(url_pesquisa, headers=cabecalho,
                                   cookies=meus_cookies) # é possível mudar o cabeçalho com parametros
    #exemplo cabecalho = {'User-agent': 'Windows 12', 'Referer': 'https://google.com'}
    #exemplo r = requests.get(url_pesquisa, headers=cabecalho)

    #User-agent indica o navegado que está usando, existem padroes
    #Referer indica de onde você clicou para acessar a pagina

    soup = BeautifulSoup(r.text, 'html.parser')
    
except Exception as e:
    print('Requisição deu erro:', e)


sair = 0

while sair == 0:
    print('Escolha uma opção:')
    opc = int(input('    1)header\n    2)status code\n    3)text\n    4)sair\n'))
    
    if opc == 1:
        print(r.headers)
    elif opc == 2:
        print(r.status_code)
    elif opc == 3:
        tag_a = soup.find_all('a')
        print(tag_a)
    elif opc == 4:
        sair = 1
    else:
        print('erro')

    print()
    input('Pressione qualquer tecla para continuar')
    print()
    opc = 0
