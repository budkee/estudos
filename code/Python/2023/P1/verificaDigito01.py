num = int(input("Digite um número inteiro: "))

# Inicialmente, definimos o último dígito como um valor que não pode aparecer no número
ultimo_digito = 10

# Percorremos os dígitos do número da direita para a esquerda
while num > 0:
    digito = num % 10
    num //= 10

    # Verificamos se o dígito atual é igual ao último dígito
    if digito == ultimo_digito:
        print("sim")
        break

    # Atualizamos o último dígito para o dígito atual
    ultimo_digito = digito
else:
    print("não")