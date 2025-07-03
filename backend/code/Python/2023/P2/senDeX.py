# Passo 1: leia x e epsilon
x = float(input())
epsilon = float(input())
# Passo 2: compute a função exponencial
numerador = x
denominador = 1
termo = numerador/denominador
soma = 0
i = 1 # Iteração da soma
sinal = -1 # Alternância do sinal
while epsilon < abs(termo):
    soma += termo
    numerador = numerador * x * x
    denominador = denominador * (2*i) * (2*i+1)
    termo = sinal * (numerador / denominador)
    sinal = (-1) * sinal
    i += 1

print('sen({0:+8.6f}) = {1:+8.6f}'.format(x, soma))
