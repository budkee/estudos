# Arquivo para executar testes

# Web Scrapping | Muito erro
## Requests: Requisicoes web
import requests

## Pandas
import pandas as pd

header = {'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

url = 'https://br.investing.com/equities/brazil'
request = requests.get(url, headers = header)

dataframe = pd.read_html(request.text)
print(dataframe)
