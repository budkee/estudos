# Soma de dois vetores
# Leia os vetores
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Leia o tamanho da lista
tam = len(a)

# Inicie a lista da soma
c = []

for i in range(tam):
    soma = a[i] + b[i]
    c.append(soma)

print(c)