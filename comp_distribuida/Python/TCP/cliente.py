import socket

# Configurar o host e a porta
host = '192.168.100.113' ## IP da máquina que deseja conectar
port = 7777  ## Acima de 5000

# Criar um objeto socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor
client_socket.connect((host, port))
print('Conectado ao servidor')

# Realizar a comunicação com o servidor
while True:
    # Enviar mensagem ao servidor
    message = input('Digite uma mensagem (Ou "sair" para sair): ')
    client_socket.send(message.encode())
    
    # Receber resposta do servidor
    response = client_socket.recv(1024).decode()
    print('Servidor:', response)

    # Verifica se o usuário deseja sair
    if message.lower() == 'sair':
        break

# Encerrar a conexão
client_socket.close()