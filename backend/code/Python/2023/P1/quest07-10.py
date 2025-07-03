# descrição das variáveis utilizadas
# int soma
soma = 0
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(i, j + 1):
            soma = soma + i + j + k
print(soma)
