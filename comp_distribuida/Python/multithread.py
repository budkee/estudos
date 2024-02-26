import _thread
import socket

# Função chamada quando uma nova thread for iniciada
def conectado(con, cliente):
    print('\nCliente conectado:', cliente)
 
    while True:
        # Recebendo as mensagens através da conexão
        msg = con.recv(1024)
        if not msg:
            break
 
        print('\nCliente..:', cliente)
        print('Mensagem.:', msg)
 
    print('\nFinalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()
 

if __name__ == '__main__':

    # Configurar o host e a porta
    host = '192.168.0.40' ## IP da sua máquina
    port = 7777 ## Acima de 5000

    # Criar um objeto socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincular o objeto socket ao host e à porta
    server_socket.bind((host, port))

    # Colocar o objeto socket em modo de escuta
    server_socket.listen(1)
    print('Aguardando conexão do cliente...')
    
    # Aceitar a conexão do cliente
    #client_socket, client_address = server_socket.accept()
    #print('Conexão estabelecida com:', client_address)

    # Loop principal
    while True:

        # Aceitando uma nova conexão
        con, cliente = server_socket.accept()
        print('\nNova thread iniciada para essa conexão')
 
        # Abrindo uma thread para a conexão
        _thread.start_new_thread(conectado, tuple([con, cliente]))

    # Fecha o socket do servidor
    server_socket.close()

