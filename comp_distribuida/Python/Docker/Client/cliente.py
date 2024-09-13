import socket
import json

def OpClient(data_operacao, conta_cliente, tipo, valor_operacao):
    request_transacao = {
        "data_operacao": data_operacao,
        "conta_cliente": conta_cliente,
        "tipo": tipo,
        "valor_operacao": valor_operacao
    }
    return json.dumps(request_transacao)

def main():
    # Configurações de Conexão
    host = 'coordenador'
    port = 7777

    # Socket TCP/IP para o cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conexão com o servidor
        client_socket.connect((host, port))
        print("[*] Conexão estabelecida com o servidor.")
            
        # Enviar dados de teste
        data_operacao = "29-02-24"
        conta_cliente = "007"
        tipo = "C"
        valor_operacao = "700"

        # Chama o método OpClient do Cliente
        data = OpClient(data_operacao, conta_cliente, tipo, valor_operacao)
        
        # Envio da requisição ao Coordenador
        try:

            client_socket.sendto(data.encode(), (host, port))

            # Pega a resposta e o endereço
            response = client_socket.recv(1024)
            server_address = client_socket.getpeername()

            # Visualiza a resposta 
            print("[*] Dados enviados com sucesso!\n")
            print(f"{data}\n")
            print(f"[*] Resposta do servidor {server_address}: {response}")

        except socket.error as e:
            print(f"Erro de comunicação com o servidor: {e}")
            conn = False  # Encerra o loop em caso de erro

    except ConnectionRefusedError:
        print("Erro: conexão recusada. Verifique se o servidor está em execução.")

    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    finally:
        client_socket.close()
        print("[*] Conexão encerrada.")

if __name__ == "__main__":
    main()
