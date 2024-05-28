# Inicialize a lista de termos
termos = []
# Inicialize o primeiro termo
termo = 0
# Inicialize o limite
lim = 10
# Calcule a sequência
while termo <= lim-1:
    eq = 2 * (termo + 1)
    termos.append(eq)
    termo += 1
# Imprima o resultado esperado [2, 4, 6, 8, 10, ..., lim * eq]
print(lim * eq)
print(termos)