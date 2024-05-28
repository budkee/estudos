# Leia a primeira lista
a = list(map(int, input().split()))
tamA = len(a)
# Leia a segunda lista
b = list(map(int, input().split()))
tamB = len(b)
# Crie a lista para o resultado
c = []
# Inicialize os índices
i, j = 0, 0
# Intercale os elementos de cada uma delas
# Enquanto i for menor que o tamanho de a e j for menor que o tamanho de b, faça:
while i < tamA and j < tamB:
    # Verifique se a[i] é menor que b[j]:
    if a[i] <= b[j]:
        # Adicione à c
        c.append(a[i])
        # feche o loop
        i += 1
    # Caso não seja, faça:
    else:
        # Adicione o elemento de b em c
        c.append(b[j])
        # Feche o loop
        j += 1    
# Junte a lista
c = c + a[i::] + b[j::]

# Imprima o resultado
print(c)