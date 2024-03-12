import requests
resposta_python = requests.get("https://pt.wikipedia.org/wiki/Python")
texto_python = resposta_python.text
print(texto_python)
