# Este programa recebe uma quantidade tam de numeros inteiros e retorna o segundo maior valor de uma lista

# Passo 1: Leia a lista de números
# Entrada na mesma linha: lista = list(map(float, input().split()))
lista = []
soma = 0
altura = float(input())
lista.append(altura)
while altura > 0:
    altura = float(input())
    lista.append(altura)
# Passo 2: Compute a média
media = sum(lista) / (len(lista)-1)
# Passo 2.1:
for altura in lista:
    if altura > media:
        soma += 1
# Passo 3: Imprima o resultado
print('{:.2f}'.format(media))
print('{}'.format(soma))
