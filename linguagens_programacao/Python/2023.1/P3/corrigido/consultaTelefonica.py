def buscar_numero_telefone(lista_telefonica, nome, sobrenome):
    for assinante in lista_telefonica:
        if assinante["nome"] == nome and assinante["sobrenome"] == sobrenome:
            return assinante["telefone"]
    return None

# Obtenha o número de assinantes a partir da entrada
num = int(input("Digite o número de assinantes: "))

# Crie a lista telefônica
lista_telefonica = []

# Leia os dados dos assinantes e armazene na lista telefônica
for _ in range(num):

    sobrenome = input("Digite o sobrenome do assinante: ")
    nome = input("Digite o nome do assinante: ")
    telefone = input("Digite o número de telefone do assinante: ")
    assinante = {"sobrenome": sobrenome, "nome": nome, "telefone": telefone}
    lista_telefonica.append(assinante)

# Obtenha o número de consultas a partir da entrada
num_consultas = int(input("Digite o número de consultas: "))

# Realize as consultas na lista telefônica
for _ in range(num_consultas):

    sobrenome_consulta = input("Digite o sobrenome do assinante a ser consultado: ")
    nome_consulta = input("Digite o nome do assinante a ser consultado: ")

    numero_telefone = buscar_numero_telefone(lista_telefonica, nome_consulta, sobrenome_consulta)

    if numero_telefone:
        print(f"Nome: {nome_consulta}")
        print(f"Sobrenome: {sobrenome_consulta}")
        print(f"Telefone: {numero_telefone}")
    else:
        print("Nome não encontrado na lista telefônica")

    print()

