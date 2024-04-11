import pip._vendor.requests

from bs4 import BeautifulSoup

def remove_h2_tags(url):
    try:
        # Obter o conteúdo da página web
        response = requests.get(url)
        response.raise_for_status()  # Verificar se houve algum erro ao obter a página

        # Criar um objeto BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remover os elementos <h2> da página
        for h2_tag in soup.find_all('h2'):
            h2_tag.extract()

        # Retornar o HTML resultante sem os elementos <h2>
        return str(soup)

    except requests.exceptions.RequestException as e:
        print("Ocorreu um erro ao obter a página:", e)
        return None

# Exemplo de uso:
url = 'https://www.ic.unicamp.br/~lehilton/cursos/1s2022/mc102w/python_c/00-intro/'  # Substitua pela URL desejada
html_without_h2 = remove_h2_tags(url)
if html_without_h2:
    print(html_without_h2)
