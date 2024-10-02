import socket
import json
import threading
from queue import Queue

def processar_solicitacao_do_cliente(client_socket, address, request_queue):
    data = client_socket.recv(1024).decode()
    request = json.loads(data)
    
    tipo_operacao = request["tipo_operacao"]
    valor_operacao = request["valor_operacao"]
    
    if tipo_operacao == "C":
        request_queue.put(("shardA", tipo_operacao, valor_operacao))
    elif tipo_operacao == "D":
        request_queue.put(("shardB", tipo_operacao, valor_operacao))
    else:
        client_socket.send("Tipo de operação inválido".encode())
        client_socket.close()
        return
    
    response = "OK"
    client_socket.send(response.encode())
    client_socket.close()

def enviar_request_para_shard(host, port, tipo_operacao, valor_operacao):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        request = {
            "tipo_operacao": tipo_operacao,
            "valor_operacao": valor_operacao
        }
        s.sendall(json.dumps(request).encode())
        response = s.recv(1024)
    return response.decode()

def processar_fila(request_queue):
    while True:
        if not request_queue.empty():
            shard, tipo_operacao, valor_operacao = request_queue.get()
            if shard == "shardA":
                response = enviar_request_para_shard('localhost', 8889, tipo_operacao, valor_operacao)
            elif shard == "shardB":
                response = enviar_request_para_shard('localhost', 8890, tipo_operacao, valor_operacao)
            else:
                response = "Shard inválido"
            print("Resposta do", shard, ":", response)

def iniciar_servidor_principal(host, port):
    request_queue = Queue()
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print("Servidor principal escutando em", (host, port))
        
        process_thread = threading.Thread(target=processar_fila, args=(request_queue,))
        process_thread.start()
        
        while True:
            client_socket, address = server_socket.accept()
            print("Conexão estabelecida com", address)
            client_thread = threading.Thread(target=processar_solicitacao_do_cliente, args=(client_socket, address, request_queue))
            client_thread.start()

if __name__ == "__main__":
    iniciar_servidor_principal('localhost', 8888)
