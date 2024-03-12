
def ehMaior(tam, lista):
    msg = 'sim'
    i = 0
    while i < tam-1:
    #for i in range(tam-1):
        if lista[0] <= lista[i+1]:
            msg = 'não'
            i = tam
        i += 1
    return print(msg)

tam = int(input())
lista = list(map(int, input(). split()))
ehMaior(tam, lista)