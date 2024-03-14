def raizq(numero, epsilon, aprox):
    while True:
        nova_aprox = (aprox + numero/aprox) / 2.0
        if abs(aprox - nova_aprox) < epsilon:
            return nova_aprox
        aprox = nova_aprox

# Obtenha os valores de entrada
numero = float(input("Digite um número real positivo: "))
epsilon = float(input("Digite um número real epsilon (0 < epsilon < 1): "))
aprox = float(input("Digite um número real para a aproximação inicial: "))

# Calcule a raiz quadrada aproximada
raiz_aproximada = raizq(numero, epsilon, aprox)

# Imprima o resultado
print(f"A raiz quadrada aproximada de {numero} é: {raiz_aproximada:6f}")
