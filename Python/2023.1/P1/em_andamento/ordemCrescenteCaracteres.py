# Função para ordenar strings por ordem alfabética
# Status: em andamento
def ordenaAlfabeto(lista_palavras, lista_ordenada):
    # Retire a primeira letra de cada item da lista e coloque na
    for palavra in palavras:
        letra = palavras[palavra]
        temp = letra[0]
        listaOrdenada.append(temp)

    # Passo 2.1. Verifique se os caracteres estão em ordem
    if (ord(listaOrdenada[0]) < ord(listaOrdenada[1])) and (
            ord(listaOrdenada[1]) < ord(listaOrdenada[2])) and (ord(
        listaOrdenada[2]) < ord(listaOrdenada[3])):
        msg = 'ordem crescente'
    else:
        msg = 'não estão em ordem crescente'

    return msg


# Leia a quantidade de elementos
num = int(input('Quantos elementos você vai analisar?: '))

# Inicialize as listas
palavras = []
listaOrdenada = []

# Leia as palavras
for i in range(num):
    palavras[i] = list(map(str, input(f'Digite a {i+1}ª palavra: ')))


msg = ordenaAlfabeto(palavras, listaOrdenada)
print('{0:s}'.format(msg))
