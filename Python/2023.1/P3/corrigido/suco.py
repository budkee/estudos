def contar_vendas_sucos(n):
    vendas = {}

    for _ in range(n):
        sabor = input("Digite o sabor do suco vendido: ")
        if sabor in vendas:
            vendas[sabor] += 1
        else:
            vendas[sabor] = 1
    print()
    print('===' * 20)
    print("Relação dos sabores dos sucos e quantidade vendida:")
    for sabor, quantidade in vendas.items():
        print(f"{sabor}: {quantidade}")

# Obtenha o número de sucos vendidos no dia a partir da entrada
n = int(input("Digite a quantidade de sucos vendidos no dia: "))

# Chame a função para contar as vendas dos sucos
contar_vendas_sucos(n)
