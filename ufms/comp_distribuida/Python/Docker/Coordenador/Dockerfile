# Use uma imagem base Python
FROM python:3.9-slim

# Copie o código do Transaction Coordinator para o contêiner
COPY coordenador.py .

# Instale as dependências necessárias
RUN pip install --upgrade pip

# Comando a ser executado quando o contêiner for iniciado
CMD ["python", "./coordenador.py"]
