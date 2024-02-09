# Regra do programa: Este programa recebe uma quantidade tam de numeros inteiros e retorna as posições do maior e do menor inteiro dessa lista, bem como seus valores e a variação entre eles..
# Exceções: Caso haja mais de um máximo ou minimo, o programa deve retornar o menor indice dos máximos/mínimo da lista.
# Função
def maiormenor(tam, lista):

    maximo = max(lista)  # Retira o maior valor
    minimo = min(lista)  # Retira o menor valor
    var = maximo - minimo
    return print('{} {} {} {} {}'.format(lista.index(maximo), maximo, lista.index(
        minimo), minimo, var))


tam = int(input())
# Passo 1: Leia a lista de números
lista = list(map(int, input().split()))[:tam]
# Passo 2: Faça a mágica
maiormenor(tam, lista)
