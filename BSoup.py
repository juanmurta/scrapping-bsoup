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
