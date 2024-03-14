import socket
import threading
from queue import Queue
import json

#-------Função-Principal--------
def start_server(host, port):

    # Cria a fila de requisições
    request_queue = Queue()
    # Cria a fila de dados
    data_queue = Queue()

    # Conexão por streamming do coordenador
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        
        server_socket.bind((host, port))
        server_socket.listen()
        print("Coordenador escutando em", (host, port))

        # Thread 1: Execução das requisições
        process_thread = threading.Thread(target=handle_request, args=(request_queue,))
        process_thread.start()
    
        # Enquanto o servidor estiver ativo
        while True:

            # Aceita a conexão de clientes
            client_socket, address = server_socket.accept()
            print(f"[*] Conexão estabelecida com {address[0]}:{address[1]}")
            
            # Thread 2: Execução dos dados dos clientes
            client_thread = threading.Thread(target=handle_client_data, args=(client_socket, address, data_queue))
            client_thread.start()


#-------Função-para-Lidar-com-as-Requisições--------|Thread-1
def handle_request(request_queue):
    """
        Envio e recebimento de requisições de Clientes e Shards.
    """

    while True:
        # | Recebimento das Requisições
        
        # Verifique se a fila não está vazia
        if not request_queue.empty():

            # Da fila de requisições, pega o shard correspondente, o tipo e o valor da operação da fila de requisições
            shard, tipo_operacao, valor_operacao = request_queue.get()
            
        # | Envio dos dados para os shards
            if shard == "shardA":
                # Passa as informações relevantes ao shard para fazer o processamento da transação e lida com a comunicação
                response = handle_shards_conn('localhost', 8888, tipo_operacao, valor_operacao)
                print(response) # O que está sendo retornado?
                
                # Carrega a resposta do servidor (recebido no formato json) e transforma em um dicionário
                saldo_atualizado = json.loads(response)['saldo_atualizado']
                print(saldo_atualizado) # O que está sendo retornado?
                return # Volta para 
            
            elif shard == "shardB":
                response = handle_shards_conn('localhost', 9999, tipo_operacao, valor_operacao)
                saldo_atualizado = json.loads(response)['saldo_atualizado']
                return
            
            else:
                response = "Shard inválido"
            
        # | Envio dos dados para os clientes
        
        


#-------Lidar-com-Shards--------|Thread-1.1
def handle_shards_conn(host, port, request_queue):
    """
        Comunicação com os Shards e envio da requisição.
    """
    
    # Comunicação por streamming
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # Enviar os dados relevantes ao shard
        request_shard = request_queue
        
        # Converte o dicionário em JSON
        s.sendall(json.dumps(request).encode())
        
        response = s.recv(1024)
    return response.decode()


#-------Lidar-com-os-Dados-do-Clientes--------|Thread-2
def handle_client_data(client_socket, address, request_queue):
    """
        Recebimento e envio de dados dos Clientes.
    """
    
    # Recebe dados do cliente
    dados = client_socket.recv(1024).decode('utf-8')
    
    # Carrega a resposta do cliente (recebido no formato json) e transforma em um dicionário
    request = json.loads(dados)
    
    # Receber o resultado do shard
    resultado = {}

    # Tratamento da mensagem
    try:
        # Tratamento da mensagem | Recebimento

        # Puxa os dados de interesse da requisição
        data_operacao = request['data_operacao']
        conta_cliente = request['conta_cliente']
        tipo_operacao = request['tipo_operacao']
        valor_operacao = request['valor_operacao']

        # Verifica qual é o tipo de operação de interesse ao usuário
        if tipo_operacao == 'C':
            request_queue.put(("shardA", tipo_operacao, valor_operacao, resultado))
        
        elif tipo_operacao == "D":
            resultado = {}
            request_queue.put(("shardB", tipo_operacao, valor_operacao, resultado))


        else:
            client_socket.send("Tipo de operação inválido".encode())
            client_socket.close()
            return
        
        # Tratamento da mensagem | Envio

        # Puxa os dados de interesse da resposta (vem do handle_request que por sua vez recebe do handle_shards_conn)

        # Atualizar o saldo
        # Obter a resposta do shard correspondente
        # O resultado será atualizado no marcador
        if 'response' in resultado:
            response = resultado['response']
            saldo_atualizado = json.loads(response)['saldo_atualizado']

            # Enviando resposta de volta para o cliente
            response = f"Transação concluída com sucesso!\n Saldo atual: {saldo_atualizado}"
            client_socket.send(response.encode('utf-8'))

            # Fechando a conexão com o cliente
            client_socket.close()

    except json.JSONDecodeError:
        response = "Erro ao decodificar JSON."


#-------Módulo-Principal--------
if __name__ == "__main__":

    # Configurações do servidor
    host = '0.0.0.0'
    port = 7777

    #-------Início-do-Programa----- 
    start_server(host, port)
