import mysql.connector
import time

# Espera 5 segundos pro db ficar pronto para conecxões
time.sleep(15)

# Cria a conexao com o servidor
conexao = mysql.connector.connect(
    host="mysql",
    user="siriusb",
    password="sirius",
    database="open_weather_map"
)

try:
    
    db_info = conexao.get_server_info()
    print("Conectado com sucesso ao servidor MySQL versão ", db_info)
    
    # Criar o cursor e verificar a conexão
    cursor = conexao.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)
    
    # Criar uma tabela e executar o DDL
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp TIMESTAMP,
        temperatura FLOAT,
        umidade INT,
        pressao_atmosferica INT,
        direcao_vento FLOAT,
        velocidade_vento FLOAT
    )""")
    print("Tabela teste criada com sucesso!")
except mysql.connector.Error as erro:
    print("Falha ao executar o DDL no servidor: ".format(erro))
finally:
    if (conexao.is_connected()):
        cursor.close()
        conexao.close()
        print("Conexão finalizada.")