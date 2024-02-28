import socket

# 1. Configurar o host e a porta
host = '0.0.0.0' ## IP da sua máquina
port = 7777 ## Acima de 5000

# 2. Criar um objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Vincular o objeto socket ao host e à porta
server_socket.bind((host, port))

# 4. Colocar o objeto socket em modo de escuta
server_socket.listen(1)
print('Aguardando conexão do cliente...')

# 5. Aceitar a conexão do cliente
client_socket, client_address = server_socket.accept()
print('Conexão estabelecida com:', client_address)

# 6. Realizar a comunicação com o cliente
while True:
    # Receber dados do cliente
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print('Cliente:', data)
    
    # Enviar resposta ao cliente
    response = input('Digite a resposta: ')
    client_socket.send(response.encode())

# Encerrar a conexão
client_socket.close()
server_socket.close()
