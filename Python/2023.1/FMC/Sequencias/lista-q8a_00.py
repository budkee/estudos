# Inicialize a lista para armazenar todos os termos, o indice i e atribua o primeiro termo ao indice i
termos = []
termo = 0
lim = 10
# Construa a sequência
while termo <= lim-1:
    termos.append(termo+1)
    termo += 1
# Imprima o resultado esperado [1,2,3,4,5,6,...,n+1]
print(termos)