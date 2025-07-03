# leitura dos números de entrada
inicio = int(input())
fim = int(input())

# inicialização da variável de soma
soma = 0

# percorre todos os números entre inicio e fim
for i in range(inicio, fim+1):
    # verifica se o número i está no intervalo desejado
    if inicio <= i <= fim:
        # adiciona o número à soma
        soma += i

# imprime o resultado
print(soma)