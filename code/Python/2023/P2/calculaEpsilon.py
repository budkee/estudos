# Passo 1: leia x e epsilon
x = float(input())
epsilon = float(input())
# Passo 2: compute a função exponencial
numerador = 1
denominador = 1
termo = numerador/denominador
soma = 0
i = 1
while epsilon <= termo:
    soma += termo
    print(f'soma = {soma}')
    numerador = x ** i
    print(f'numerador = {numerador}')
    denominador = denominador * i
    print(f'denominador = {denominador}')
    termo = numerador/denominador
    print(f'termo = {termo}')

    i += 1
print('{0:.7f}'.format(soma))
