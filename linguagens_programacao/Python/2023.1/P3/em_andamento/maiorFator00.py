def maxfator(numero):
    if numero <= 1:
        return abs(numero)

    for fator in range(numero - 1, 1, -1):
        if numero % fator == 0:
            return fator

    return abs(numero)

# Obtenha o número inteiro da entrada
n = int(input("Digite um número inteiro (|n| > 1): "))

# Calcule o maior fator do número e imprima o resultado
maior_fator = maxfator(n)
print("Número:", n)
print("Maior Fator:", maior_fator)
