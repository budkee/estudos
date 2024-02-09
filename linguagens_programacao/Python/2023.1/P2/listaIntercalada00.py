# Leia a primeira lista
listaA = list(map(int, input().split()))
# Leia a segunda lista
listaB = list(map(int, input().split()))
# Crie a lista para o resultado
listaC = []

# Intercale os elementos de cada uma delas
for i in range(0, len(listaA)):
    listaC.append(listaA[i])
    listaC.append(listaB[i])
    
# Imprima o resultado
print(listaC)