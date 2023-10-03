from criaLista import divisores
lista = divisores(int(input('')))
def soma():
    soma = 0
    for num in lista:
        soma += num
        print(soma)
    return soma


print(soma())
