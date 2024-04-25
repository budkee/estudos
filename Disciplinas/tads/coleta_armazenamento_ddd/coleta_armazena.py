import os
import sys
import json
import pandas as pd
import mysql.connector

# Ler o arquivo JSON
with open('dados.json', 'r') as file:
    data = json.load(file)

# Estabelecer conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Criar uma tabela (caso não exista) para armazenar os dados do JSON
cursor.execute("""
CREATE TABLE IF NOT EXISTS tabela_json (
    id INT AUTO_INCREMENT PRIMARY KEY,
    campo1 VARCHAR(255),
    campo2 INT,
    campo3 VARCHAR(255)
)
""")

# Inserir os dados do JSON na tabela
for item in data:
    query = "INSERT INTO tabela_json (campo1, campo2, campo3) VALUES (%s, %s, %s)"
    valores = (item['campo1'], item['campo2'], item['campo3'])
    cursor.execute(query, valores)

# Commit para salvar as alterações
conexao.commit()

# Fechar cursor e conexão
cursor.close()
conexao.close()
