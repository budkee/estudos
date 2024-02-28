import socket
import threading

def handle_client(client_socket, client_address):
    """
    Função para lidar com a conexão de um cliente.
    """
    print('\n|ˆ-ˆ| Conexão estabelecida com:', client_address)

    try:
        while True:
            data = client_socket.recv(1024).decode()

            if not data:
                break

            if data.lower() == "sair":
                print(f"\n|-_-| Cliente {client_socket.getpeername()} desconectado")
                break

            print(f"|ˆ-ˆ| Mensagem recebida do cliente {client_address}: {data}")

            response = 'Ok'
            client_socket.send(response.encode())

    except ConnectionResetError:
        print(f"\n|-_-| Cliente {client_socket.getpeername()} desconectado abruptamente.")

    finally:
        client_socket.close()
        print('|-|-| Cliente desconectado:', client_address)
        print("|-|-| Threads ativas:", threading.active_count() - 1)
        print("|-|-| Lista de threads ativas:\n")
        for thread in threading.enumerate():
            if thread != threading.current_thread():
                print(f"| * | {thread.name}")

def accept_clients(server_socket):
    """
    Função para aceitar conexões de clientes e criar threads para lidar com eles.
    """
    threads = []

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print("\n|ˆ-ˆ| Número de threads ativas:", threading.active_count())
            print("|-|-| Lista de threads ativas:\n")
            for thread in threading.enumerate():
                if thread != threading.current_thread():
                    print(f"| * | {thread.name}")

            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
            
            threads.append(client_thread)
            threads = [t for t in threads if t.is_alive()]

    except Exception as e:
        print(f"Erro inesperado: {e}")

def main():
    """
    Função principal para configurar o servidor.
    """
    # Configurar o host e a porta
    host = '0.0.0.0'
    port = 7777

    # Criar um objeto socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Vincular o objeto socket ao host e à porta
        server_socket.bind((host, port))

        # Colocar o objeto socket em modo de escuta
        server_socket.listen()
        print('|ˆ-ˆ| Aguardando conexões de clientes...')

        accept_clients(server_socket)

    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")

    finally:
        # Encerrar o socket do servidor
        server_socket.close()
        print("\n| ^_^ | Servidor encerrado.")

if __name__ == "__main__":
    main()
