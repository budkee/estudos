# Use a imagem base Alpine Linux
FROM python:alpine

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos necessários
COPY test/requirements.txt .
COPY test/script.py .

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "script.py"]

#CMD ["python", "coleta_armazena.py", "--coord", "-20.45", "-54.56", "--out", "dados_coletados.json"]
