# Inicialize a lista de termos
termos = []
# Inicialize o primeiro termo
termo = 1
# Declare o limite da lista
lim = 10
# Calcule a sequência
while termo <= lim:
    eq = termo
    termos.append(termo)
    termo += 1
# Imprima o resultado esperado [1,2,3,4,5,6, ..., lim*eq]
print(termos)