def handle_client(client_socket):
    
    # Recebe dados do cliente
    client_request = client_socket.recv(1024).decode('utf-8')

    # Fila de clientes e identificação por ordem de chegada
    print(f"Dados recebidos do cliente[{addr[0]}]: {request}")

    # Trata a mensagem 
    try:
        
        client_data = json.loads(request)
        
        # Verifica se é uma operação
        if "operation" in client_data and client_data["operation"] == "OpClient":
            
            # Extrai os dados relevantes
            client_data = {

                "data": client_data["data"],
                "conta_cliente": client_data["conta_cliente"],
                "type": client_data["type"],
                "value": client_data["value"]
            
            }

            # Armazena os dados em um arquivo JSON (ou deixa armazenado em cache?)
            with open("client_data.json", "a") as json_file:

                json.dump(client_data, json_file)
                json_file.write("\n")

            response = "OK"

        else:
            # Caso solicite um tipo diferente do permitido
            response = "Operação não suportada."
    except json.JSONDecodeError:
        response = "Erro ao decodificar JSON."

    # Envia resposta de volta para o cliente
    client_socket.send(response.encode('utf-8'))

    # Deseja realizar uma nova transação? (a implementar)
    ## Sugestão de implementação: Menu de opções ao usuário, para dar opção de (1) realizar uma nova transação e (2) encerrar a conexão;

    # Fecha a conexão com o cliente
    client_socket.close()


def handle_shards(shard_socket):
    
    # Recebe dados do servidor
    shard_request = shard_socket.recv(1024).decode('utf-8')

    # Identificação 
    print(f"Dados recebidos do shard[{addr[0]}]: {request}")

    # Trata a mensagem 
    try:
        
        client_data = json.loads(request)
        
        # Verifica se é uma operação
        if "operation" in client_data and client_data["operation"] == "OpClient":
            
            # Extrai os dados relevantes
            client_data = {

                "data": client_data["data"],
                "conta_cliente": client_data["conta_cliente"],
                "type": client_data["type"],
                "value": client_data["value"]
            
            }

            # Armazena os dados em um arquivo JSON (ou deixa armazenado em cache?)
            with open("client_data.json", "a") as json_file:

                json.dump(client_data, json_file)
                json_file.write("\n")

            response = "OK"

        else:
            # Caso solicite um tipo diferente do permitido
            response = "Operação não suportada."
    except json.JSONDecodeError:
        response = "Erro ao decodificar JSON."

    # Envia resposta de volta para o cliente
    client_socket.send(response.encode('utf-8'))

    # Deseja realizar uma nova transação? (a implementar)
    ## Sugestão de implementação: Menu de opções ao usuário, para dar opção de (1) realizar uma nova transação e (2) encerrar a conexão;

    # Fecha a conexão com o cliente
    client_socket.close()