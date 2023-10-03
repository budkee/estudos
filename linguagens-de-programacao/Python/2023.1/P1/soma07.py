# No caso de calcular o número de elementos num conjunto que tem uma certa propriedade, podemos usar um generator com as instruções for e if e depois aplicar a função sum() para obter o número de consoantes numa dada palavra composta com caracteres do alfabeto.
palavra = str(input())
vogais = 'AEIOUaeiou'
numcons = 0
for letra in palavra:
    if letra not in vogais:
        numcons += 1
print(numcons)
