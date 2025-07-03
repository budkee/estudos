# Digite o inteiro de interesse
n = int(input())
# Inicialize a lista de divisores de n
div = [1]
# Candidato a divisor
c = 2
# Gere todos os candidatos, divisores de n, e teste cada um deles
while c <= n:
    # Se o candidato (c) for divisor de n, adicione a lista:
    if c % n == 0:
        div.append(c)
    # Próximo candidato
    c += 1
# Imprime a lista dos divisores
print(div)
