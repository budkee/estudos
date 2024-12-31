import socket
import threading

def handle_clients_conn(client_socket, client_address):
    """
    Função para lidar com a conexão de vários clientes.
    """
    print(f"|^-^| Cliente conectado: {client_address}")

    try:
        while True:
            # Receber dados do cliente
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Cliente {client_address} enviou: {data.decode('utf-8')}")

            # Responder ao cliente
            client_socket.sendall("Mensagem recebida!".encode('utf-8'))
    except Exception as e:
        print(f"Erro ao lidar com a conexão do cliente {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"|T_T| Cliente desconectado: {client_address}")


def handle_servers_msg(server_socket, server_address):
    """
    Função para lidar com a conexão de vários servidores.
    """
    print(f"|^-^| Conectado ao servidor: {server_address}")

    try:
        while True:
            # Enviar dados ao servidor 

            # Receber dados do servidor
            data = server_socket.recv(1024)
            if not data:
                break
            print(f"Servidor {server_address} enviou: {data.decode('utf-8')}")

            # Responder ao servidor
            server_socket.sendall("Mensagem recebida!".encode('utf-8'))
    except Exception as e:
        print(f"Erro ao lidar com a conexão do servidor {server_address}: {e}")
    finally:
        server_socket.close()
        print(f"|T_T| Servidor desconectado: {server_address}")


def accept_clients(host_socket):
    """
    Função para aceitar conexões de clientes e servidores e criar threads para lidar com eles.
    """
    try:
        while True:
            # Aceitar conexão do cliente
            client_socket, client_address = host_socket.accept()

            # Criar uma nova thread para lidar com o cliente
            client_thread = threading.Thread(target=handle_clients_conn, args=(client_socket, client_address))
            client_thread.start()

            # Aceitar conexão do servidor
            server_socket, server_address = host_socket.accept()

            # Criar uma nova thread para lidar com o servidor
            server_thread = threading.Thread(target=handle_servers_conn, args=(server_socket, server_address))
            server_thread.start()

    except Exception as e:
        print(f"Erro ao aceitar conexões: {e}")

def main():

    # ------------Início-do-Programa---------------
    # Configurar o host e a porta de escuta
    host = '0.0.0.0'
    port = 7777

    # Comunicação em TCP/IP
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        #server_address = host_socket.bind()

        # Vincular o socket ao endereço e à porta
        host_socket.bind((host, port))

        # Colocar o socket em modo de escuta
        host_socket.listen()
        print('|ˆ-ˆ| Aguardando conexões de clientes...')

        # Aceitar clientes e servidores de modo assíncrono
        accept_clients(host_socket)

    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")

    finally:
        # Encerrar o socket do servidor
        host_socket.close()
        print("\n| ^_^ | Servidor encerrado.")

if __name__ == "__main__":
    main()
