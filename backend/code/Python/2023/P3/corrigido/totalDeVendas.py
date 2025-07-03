def calcular_vendas_totais(vendas, precos):
    # Inicializar listas de total de vendas por vendedor e total de vendas
    vendas_totais_vendedor = [0] * len(vendas)
    total_vendas = 0

    # Calcular o total de vendas por vendedor e o total de vendas da revenda
    for vendedor in range(len(vendas)):
        for modelo in range(len(vendas[vendedor])):
            quantidade = vendas[vendedor][modelo]
            preco = precos[modelo]
            vendas_totais_vendedor[vendedor] += quantidade * preco
            total_vendas += quantidade * preco

    return vendas_totais_vendedor, total_vendas


# Ler as dimensões da tabela de vendas e os dados das vendas
m, n = map(int, input("Digite as dimensões m e n da tabela de vendas: ").split())

vendas = []
for _ in range(m):
    linha = list(map(int, input().split()))
    vendas.append(linha)

# Ler os preços de venda dos modelos
precos = list(map(float, input("Digite os valores de venda de cada modelo: ").split()))

# Calcular as vendas totais por vendedor e a venda total da revenda
vendas_totais_vendedor, total_vendas = calcular_vendas_totais(vendas, precos)

# Imprimir os resultados
print("Vendedor     Total de Vendas")
for vendedor, total in enumerate(vendas_totais_vendedor):
    print('{0:5d} R${1:12.2f}'.format(vendedor + 1, total))
print('Total R${0:12.2f}'.format(total_vendas))
