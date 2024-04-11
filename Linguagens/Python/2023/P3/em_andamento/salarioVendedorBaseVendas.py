def calcular_salario_semanal(vendas, precos):
    # Inicializar lista de salários semanais
    salarios_semanais = []

    # Calcular o total vendido por cada vendedor
    for vendedor in vendas:
        total_vendido = 0
        for i, quantidade in enumerate(vendedor):
            total_vendido += quantidade * precos[i]

        # Calcular o salário semanal do vendedor (comissão + salário fixo)
        salario_semanal = total_vendido * 0.1 + 200
        salarios_semanais.append(salario_semanal)

    return salarios_semanais


# Ler o número de vendedores e a quantidade de itens comercializados
num, prod = map(int, input("Digite o número de vendedores e a quantidade de itens: ").split())

# Ler as vendas de cada vendedor
vendas = []
for _ in range(num):
    linha = list(map(int, input().split()))
    vendas.append(linha)

# Ler os preços de venda dos itens
precos = list(map(float, input("Digite os valores de venda de cada item: ").split()))

# Calcular os salários semanais dos vendedores
salarios_semanais = calcular_salario_semanal(vendas, precos)

# Imprimir a tabela de salários semanais
print("Vendedor  Salário Semanal")
for vendedor, salario in enumerate(salarios_semanais):
    print('{0:8d}  R${1:10.2f}'.format(vendedor + 1, salario))
