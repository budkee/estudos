import threading
import socket
import json


def handle_request(coord_socket, address):
    # Recebe os dados do coordenador
    data = coord_socket.recv(1024).decode()
    request = json.loads(data)
    
    # Puxa os dados de interesse
    tipo_operacao = request["tipo_operacao"]
    valor_operacao = request["valor_operacao"]
    
    # Simulação de operação de crédito
    saldo_atualizado = 1000 + valor_operacao
    
    # Retorna pro coordenador
    response = f"OK!\n Saldo atualizado: {saldo_atualizado}"
    coord_socket.send(json.dumps(response).encode())
    coord_socket.close()


def shard_a(host, port):
    
    # Conexão por streamming
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print("Servidor shardA escutando em", (host, port))
        
        while True:
            coord_socket, address = server_socket.accept()
            print(f"[*] Conexão estabelecida com {address[0]}:{address[1]}")
            coord_thread = threading.Thread(target=handle_request, args=(coord_socket, address))
            coord_thread.start()


if __name__ == "__main__":
    
    # lendo ip do coordenator
    host = '0.0.0.0'#'coordenador'
    port = 8888  
    
    shard_a(host, port)
