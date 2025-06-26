# Sobre:
# O programa a seguir realiza a leitura de 5 caracteres em letras maiúsculas(codificada) e o seu deslocamento(chave) dentro do intervalo e retorna a mensagem decodificada.

# Passo 1: leitura das entradas
msg = str(input())
deslocamento = int(input())
# Passo 2: Decodificação
for letra in msg:
    deCod = chr((ord(letra) - ord('A') - deslocamento) % 26 + ord('A'))
    # print(deCod)
    # Passo 3: Imprima o resultado em uma só linha
    print('{0}'.format(deCod), end='')
