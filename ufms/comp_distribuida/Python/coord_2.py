import socket
import threading
import queue
import time

# Configurações do servidor
HOST = '0.0.0.0'  # Escuta em todas as interfaces de rede
PORT = 7777       # Porta que o servidor vai escutar
max_connections = 5

# Fila para armazenar conexões de clientes
client_queue = queue.Queue()

# 1.2.1. Função para lidar com a conexão de um cliente
def handle_client(client_socket, address):
    print(f"Conexão estabelecida com {address}")
    
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Mensagem recebida do cliente {address}: {data.decode()}")
            
            # Aqui você pode processar a mensagem ou enviar para outros servidores shards, etc.
            response = b"Recebido pelo servidor principal: " + data
            
            # Envia uma resposta de volta para o cliente
            client_socket.sendall(response)
    
    print(f"Conexão com {address} fechada")

# Função para estabelecer uma conexão de socket com um shard
def connect_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.0.40', 7777))
    return s

# Função para lidar com a conexão de um shard
def handle_shard(shard_socket, address):
    print(f"Conexão estabelecida com shard {address}")
    
    with shard_socket:
        while True:
            data = shard_socket.recv(1024)
            if not data:
                break
            print(f"Mensagem recebida do shard {address}: {data.decode()}")
            
            # Aqui você pode processar a mensagem recebida do shard, se necessário
            response = b"Recebido pelo servidor principal do shard: " + data
            
            # Envia uma resposta de volta para o shard
            shard_socket.sendall(response)
    
    print(f"Conexão com shard {address} fechada")

# Função para aceitar conexões de clientes e adicionar à fila
def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()
        client_queue.put((client_socket, client_address))

# Função para lidar com as conexões de clientes na fila
def handle_client_queue():
    while True:
        client_socket, client_address = client_queue.get()
        handle_client(client_socket, client_address)
        client_queue.task_done()

# Cria um objeto de socket do tipo TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket ao endereço e porta especificados
server_socket.bind((HOST, PORT))

# Define o limite máximo de conexões pendentes
server_socket.listen(max_connections)

print(f"Servidor escutando em {HOST}:{PORT}")

# Inicia uma thread para aceitar conexões de clientes
accept_thread = threading.Thread(target=accept_clients)
accept_thread.start()

# Inicia várias threads para lidar com as conexões de clientes na fila
for _ in range(max_connections):
    client_handler_thread = threading.Thread(target=handle_client_queue)
    client_handler_thread.daemon = True
    client_handler_thread.start()

# Exemplo de uso de uma conexão de socket com um shard
def use_socket(sock):
    print("Using socket:", sock)
    time.sleep(2)  # Simula alguma operação de uso da conexão

# Exemplo de uso de uma conexão de socket com um shard
shard_socket = connect_socket()
use_socket(shard_socket)

# O programa principal continua aqui, executando outras tarefas, etc.
# Ele não será bloqueado pelas threads que lidam com as conexões dos clientes

# Você pode esperar pelas threads de aceitação e tratamento de clientes para terminar, se necessário
accept_thread.join()
client_queue.join()

# Fechar o socket do servidor
server_socket.close()

