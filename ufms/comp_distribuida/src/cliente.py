import socket
import json

def enviar_request(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(json.dumps(request).encode())
        response = s.recv(1024)
    return response.decode()

host = 'localhost'
port = 8888

tipo_operacao = "D"
valor_operacao = 200

request_para_servidor_principal = {
    "tipo_operacao": tipo_operacao,
    "valor_operacao": valor_operacao
}

response = enviar_request(host, port, request_para_servidor_principal)
print("Resposta do servidor principal:", response)

