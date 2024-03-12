### Entradas ###

# Lista ordenada dos números dos produtos
produtos = list(map(int, input().split()))
# Tamanho da lista de produtos
tam = len(produtos)
# Lista ordenada dos preços dos proutos
precos = list(map(float, input().split()))
# Número do produto de interesse
busca = int(input())

### Busca binária ###

# Inicialize as variáveis de busca: primeiro elemento, último elemento, encontrou e mensagem.
primeiro = 0
ultimo = tam-1 # Pois a lista começa em 0
encontrou = False
msg = 'produto inexistente'

# Percorra a lista em busca do produto
while primeiro <= ultimo and not encontrou:
    # Calcule o ponto médio do intervalo, este será a nossa mira e a iteração de interesse
    meio = (primeiro + ultimo)//2 
    # Verifique em qual parte da lista o produto está
    if busca > produtos[meio]:
        primeiro = meio + 1
    elif busca < produtos[meio]:
        ultimo = meio - 1
### Saída ###

# Imprima o preço do produto de interesse
    elif busca == produtos[meio]:
        encontrou = True
        msg = '{0}'.format(precos[meio])
# Ou imprima a mensagem fora do laço
print(msg)