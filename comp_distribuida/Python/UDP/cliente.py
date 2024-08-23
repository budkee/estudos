import socket

# Define o IP e a porta do servidor UDP
ip_servidor = '192.168.64.12'
porta_servidor = 7777

# Cria um socket UDP
cliente_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Obtém a mensagem do usuário
    mensagem = input("Digite uma mensagem (ou 'sair' para sair): ")

    # Envie a mensagem para o servidor
    cliente_udp.sendto(mensagem.encode(), (ip_servidor, porta_servidor))

    # Verifica se o usuário deseja sair
    if mensagem.lower() == 'sair':
        break

    # Aguarda a resposta do servidor
    resposta, endereco_servidor = cliente_udp.recvfrom(1024)
    print(f"Resposta do servidor: {resposta.decode()}")

# Fecha o socket do cliente
cliente_udp.close()