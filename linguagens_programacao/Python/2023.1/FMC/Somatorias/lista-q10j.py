soma = 0
somaLista = []
for i in range(1,101): 
    eq = i**2
    soma += eq
    somaLista.append(eq)
print(somaLista)
print(sum(somaLista) - 5)