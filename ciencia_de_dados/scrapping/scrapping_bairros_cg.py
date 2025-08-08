import os
import time
import requests
from bs4 import BeautifulSoup
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

# URL base do site
base_url = "https://www.ruacep.com.br/ms/campo-grande/bairros"

# Função para coletar dados de uma página específica
def coletar_dados_pagina(pagina):
    url = f"{base_url}/{pagina}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Encontre os elementos contendo os dados dos bairros
        bairros = soup.find_all("div", class_="card-header")
        dados = []

        for bairro in bairros:
            nome = bairro.find("a").text.strip()
            cep_texto = bairro.find_next_sibling("div", class_="card-body").find("p", class_="card-text").text.strip()
            cep = cep_texto.replace("CEP: ", "")
            dados.append([nome, cep])

        return dados
    except requests.RequestException as e:
        print(f"Erro ao coletar dados da página {pagina}: {e}")
        return []

# Função principal para coletar dados de todas as páginas
def coletar_dados_todas_paginas():
    todos_os_dados = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(coletar_dados_pagina, pagina) for pagina in range(1, 426)]
        for future in as_completed(futures):
            try:
                dados_pagina = future.result()
                todos_os_dados.extend(dados_pagina)
            except Exception as e:
                print(f"Erro ao coletar dados: {e}")

    return todos_os_dados

# Escreva os dados em um arquivo CSV
def salvar_dados_csv(dados, filename="bairros_cg.csv"):
    try:
        modo_arquivo = 'w'  # Assume que o arquivo será aberto em modo de escrita ('w') por padrão
        if os.path.exists(filename):
            modo_arquivo = 'a'  # Se o arquivo já existe, altera para modo de anexo ('a') para adicionar dados sem reescrever o cabeçalho

        with open(filename, modo_arquivo, newline="") as csvfile:
            writer = csv.writer(csvfile)
            if modo_arquivo == 'w':  # Se estiver escrevendo um novo arquivo, escreva o cabeçalho
                writer.writerow(["Bairro", "CEP"])
            writer.writerows(dados)

    except IOError as e:
        print(f"Erro de E/S ao escrever no arquivo CSV: {e}")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados no arquivo CSV: {e}")

if __name__ == "__main__":
    print("Iniciando a coleta de dados...")
    start_time = time.time()
    todos_os_dados = coletar_dados_todas_paginas()
    salvar_dados_csv(todos_os_dados)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Tempo de execução:", elapsed_time, "segundos")
    print("Dados salvos em bairros_cg.csv")
