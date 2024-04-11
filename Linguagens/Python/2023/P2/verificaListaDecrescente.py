# Este programa verifica se uma lista está em ordem decrescente

# Passo 1: leia a lista
lista = list(map(int, input().split()))
# Passo 2: verifique se está decrescente
tam = len(lista)
valor = 'verdadeiro'
# Passo 2.1: Percorra a lista até o penúltimo elemento e verifique se cada elemento i é maior que seu sucessor (i+1)
for i in range(tam-1):
    if lista[i] <= lista[i+1]:
        valor = 'falso'
# Passo 3: imprima V ou F
print(valor)