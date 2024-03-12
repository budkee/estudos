import threading
import socket
import json

def processar_solicitacao_do_servidor_principal(client_socket, address):
    data = client_socket.recv(1024).decode()
    request = json.loads(data)
    
    tipo_operacao = request["tipo_operacao"]
    valor_operacao = request["valor_operacao"]
    
    # Simulação de operação de crédito
    saldo_atualizado = 1000 + valor_operacao
    
    response = {"saldo_atualizado": saldo_atualizado}
    client_socket.send(json.dumps(response).encode())
    client_socket.close()

def iniciar_servidor_shardA(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print("Servidor shardA escutando em", (host, port))
        
        while True:
            client_socket, address = server_socket.accept()
            print("Conexão estabelecida com", address)
            client_thread = threading.Thread(target=processar_solicitacao_do_servidor_principal, args=(client_socket, address))
            client_thread.start()

if __name__ == "__main__":
    iniciar_servidor_shardA('localhost', 8889)
