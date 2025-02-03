# from bs4 import BeautifulSoup
#
# with open('Pagina Hashtag.html', 'r', encoding='utf-8') as arquivo:
#     site = BeautifulSoup(arquivo, 'html.parser')
#
# #print(site.prettify())
# titulo = site.title
# titulo2 = site.find('title')
# titulo3 = site.find('h1')
# print(titulo3.text)
#
# barra_navegacao = site.find('nav')
# print(barra_navegacao.prettify())
#
# links = barra_navegacao.find_all('a')
# print(links)
#
# print(links[0])
# print(links[0].attrs)
# url_link = links[0]['href']
# print(url_link)
#
# for link in links:
#     print(link['href'])
#
# # procurando varios elementos
# elementos_navegacao = barra_navegacao.find_all(['a', 'button'])
# print(elementos_navegacao)
#
#
# # outras regras de find
# subtitulo = site.find(class_='tit')  # classe tem que usar sempre o _
# cabecalho = site.find(id='header')
# cabecalho2 = site.find(role='banner')
# cabecalho3 = site.find(id='header', role='banner')
# logo = site.find('img', {'data-ll-status': 'loaded'})  # se tiver ifen precisa usar como dicionario
# print(logo)
#
#
# # busca por texto exato
# foco_mercado = site.find(string='Foco no Mercado')
# print(foco_mercado)
#
# # buscar por parte do texto
# import re
#
# textos = site.find_all(string=re.compile('alunos'))
# print(textos)
#
# # parent e content
# parent = textos[0].parent.parent  # mostra elementos a cima
# print(parent)
#
# print(barra_navegacao.contents)
# for elemento in barra_navegacao.contents:
#     print(elemento)
#
# botao = barra_navegacao.contents[1]  # mostra os elementos para baixo
# titulo_alunos = site.find(id='mais-de-50-000-de-alunos-formados-por-todos-os-cursos-da-hashtag')
# print(titulo_alunos.contents)
# print(titulo_alunos.contents[0].contents)
#

# # trabalhando com site real
#
# from bs4 import BeautifulSoup
# import requests
# import re
#
# link = 'https://coinmarketcap.com/'
# requisicao = requests.get(link)
# site = BeautifulSoup(requisicao.text, 'html.parser')
#
# tbody = site.find('tbody')
# linhas = tbody.find_all('tr')
#
# for linha in linhas:
#     try:
#         print(linha.find(class_='ehyBa-d').text)
#         # print(linha.find(class_='dzgUIj').text)
#         print(linha.find(string=re.compile("\$")))
#     except AttributeError:
#         break
#
#
# # outra forma de resolver
#
# for linha in linhas:
#     texto_linha = linha.get_text(separator=';')
#     lista_textos = texto_linha.split(';')
#     nome = lista_textos[1]
#     preco = lista_textos[4]
#     print(nome, preco)


from bs4 import BeautifulSoup
import requests
import re

# URL do site que será acessado
link = 'https://coinmarketcap.com/'

# Fazendo a requisição HTTP para obter o conteúdo da página
requisicao = requests.get(link)

# Analisando o conteúdo HTML da página usando BeautifulSoup
site = BeautifulSoup(requisicao.text, 'html.parser')

tbody = site.find('tbody')
linhas = tbody.find_all('tr')

moedas = {}
for linha in linhas:
    try:
        nome = linha.find(class_='ehyBa-d').text
        codigo = linha.find(class_='coin-item-symbol').text
        valores = linha.find_all(string=re.compile(r'\$'))
        preco = valores[0]
        percentuais = linha.find_all(string=re.compile('%'))

        # Verificando se as variações percentuais são negativas e adicionando o sinal '-'
        for i, percentual in enumerate(percentuais):
            if 'ivvJzO' in percentual.parent['class']:
                percentuais[i] = '-' + str(percentual)

        var_1h = percentuais[0]
        var_24f = percentuais[1]
        var_7d = percentuais[2]

        market_cap = valores[2]
        volume = valores[3]
        dic = {'nome': nome, 'codigo': codigo, 'preco': preco, 'market_cap': market_cap,
               'volume': volume, 'var_1h': var_1h, var_24f: var_24f, 'var_7d': var_7d}
        moedas[nome] = dic
    except AttributeError:
        break

print(moedas)
