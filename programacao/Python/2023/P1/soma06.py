# No caso de calcular o número de elementos num conjunto que tem uma certa propriedade, podemos usar um generator com as instruções for e if e depois aplicar a função sum() para obter o número de consoantes numa dada palavra composta com caracteres do alfabeto.
palavra = str(input())
vogais = 'AEIOUaeiou'
numcons = 0
i = 0
while i < len(palavra):
    if palavra[i] not in vogais:
        numcons = numcons + 1
    i = i + 1
print(numcons)
