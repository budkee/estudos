import socket

HOST = '192.168.0.40'  # IP do servidor
PORT = 7777             # Porta do servidor

# Cria um objeto de socket do tipo TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
client_socket.connect((HOST, PORT))


# Envia uma mensagem ao servidor
message = "Olá, servidor!"
client_socket.sendall(message.encode())

# Recebe a resposta do servidor
data = client_socket.recv(1024)
print("Resposta do servidor:", data.decode())

# Fecha o socket
client_socket.close()
