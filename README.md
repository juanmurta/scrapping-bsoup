# Web Scraper de Dados de Criptomoedas

## Descrição
Este script utiliza a biblioteca `BeautifulSoup` para fazer scraping do site CoinMarketCap e extrair informações sobre criptomoedas, incluindo:
- Nome e código da moeda
- Preço atual
- Capitalização de mercado
- Volume de negociação
- Variações percentuais em 1 hora, 24 horas e 7 dias

Os dados são organizados em um dicionário para facilitar o acesso e manipulação.

## Como Utilizar
### Pré-requisitos
Antes de executar o script, instale as dependências necessárias:
```bash
pip install requests beautifulsoup4
```

### Executando o Script
1. Certifique-se de que tem acesso à internet, pois o script faz requisições HTTP ao site CoinMarketCap.
2. Execute o script Python:
   ```bash
   python nome_do_script.py
   ```
3. Os dados extraídos serão exibidos no console no formato de dicionário.

### Observações
- O script pode falhar se a estrutura HTML do CoinMarketCap mudar. Caso isso ocorra, será necessário atualizar as classes CSS utilizadas no `find()` e `find_all()`.
- Para evitar bloqueios por requisições excessivas, utilize técnicas como `headers` e `time.sleep()` entre requisições em caso de múltiplos acessos.
- O script extrai apenas as moedas listadas na primeira página do CoinMarketCap.

## Contribuindo para o Projeto
Caso queira contribuir com melhorias ou correções para este projeto, siga os seguintes passos:
1. Faça um fork do repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-modificacao`).
3. Faça commit das suas alterações (`git commit -m 'Melhoria no scraping'`).
4. Faça push para a branch (`git push origin minha-modificacao`).
5. Abra um Pull Request para análise.

Sinta-se à vontade para sugerir melhorias!
