# Inicialize a lista de termos
termos = []
# Inicialize o primeiro termo
termo = 1
# Inicialize o limite
lim = 10
# Calcule a sequência
while termo <= lim:
    eq = 2 * termo
    termos.append(eq)
    termo += 1
# Imprima o resultado esperado [2, 4, 6, 8, 10, ..., 2*n, ..., lim]
print(lim*eq)
print(termos)