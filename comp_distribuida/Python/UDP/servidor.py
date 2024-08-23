import socket

# Define o IP e a porta para o servidor UDP
ip_servidor = '192.168.64.12'
porta_servidor = 7777

# Cria um socket UDP
servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liga o socket à porta e endereço IP
servidor_udp.bind((ip_servidor, porta_servidor))

print(f"Servidor UDP rodando em {ip_servidor}:{porta_servidor}...")

while True:
    # Aguarda uma mensagem do cliente
    mensagem, endereco_cliente = servidor_udp.recvfrom(1024)

    # Verifica se o cliente deseja sair
    if mensagem.decode().lower() == 'sair':
        break

    # Imprime a mensagem recebida
    print(f"Mensagem recebida do cliente {endereco_cliente}: {mensagem.decode()}")

    # Envia uma resposta ao cliente
    resposta = 'Mensagem recebida com sucesso!'
    servidor_udp.sendto(resposta.encode(), endereco_cliente)

# Fecha o socket do servidor
servidor_udp.close()