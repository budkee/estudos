# Lê a mensagem e a palavra-chave da entrada padrão
message = input().upper()
keyword = input().upper()

# Transforma a palavra-chave em uma sequência de inteiros correspondentes aos códigos ASCII
key_int = [ord(c) - 64 for c in keyword]

# Inicializa o índice da palavra-chave como zero
key_index = 0

# Inicializa a mensagem criptografada como uma string vazia
encrypted = ""

# Inicializa o contador de caracteres processados
i = 0

# Enquanto ainda houver caracteres na mensagem
while i < len(message):
    # Obtém o caractere atual da mensagem
    c = message[i]

    # Transforma o caractere em seu código ASCII
    code = ord(c) - 64

    # Se o código não estiver entre 1 e 26, significa que não é uma letra maiúscula do alfabeto
    if code < 1 or code > 26:
        # Nesse caso, adiciona o caractere original à mensagem criptografada
        encrypted += c
    else:
        # Adiciona o valor correspondente da palavra-chave ao código do caractere
        new_code = (code + key_int[key_index]) % 26

        # Se o novo código for zero, substitui por 26
        if new_code == 0:
            new_code = 26

        # Transforma o novo código de volta em um caractere maiúsculo do alfabeto
        new_c = chr(new_code + 64)

        # Adiciona o novo caractere à mensagem criptografada
        encrypted += new_c

        # Avança o índice da palavra-chave para o próximo caractere
        key_index = (key_index + 1) % len(key_int)

    # Avança o contador de caracteres processados
    i += 1

# Imprime a mensagem criptografada
print(encrypted)
