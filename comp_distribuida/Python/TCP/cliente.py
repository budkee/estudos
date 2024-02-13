# 0. Imports
import socket

# 1. Configurar o host e a porta
host = '192.168.100.113' ## IP da máquina que deseja conectar
port = 7777  ## Acima de 5000

# 2. Criar um objeto socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Conectar ao servidor
client_socket.connect((host, port))
print('Conectado ao servidor')

# 4. Realizar a comunicação com o servidor
while True:
    # 4.1. Enviar mensagem ao servidor
    message = input('Digite uma mensagem (Ou "sair" para sair): ')
    client_socket.send(message.encode())
    
    # 4.2 Receber resposta do servidor
    response = client_socket.recv(1024).decode()
    print('Servidor:', response)

    # 4.3. Verifica se o usuário deseja sair
    if message.lower() == 'q':
        break

# 5. Encerrar a conexão
client_socket.close()