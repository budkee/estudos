# Método strip()
palavra = ' Algoritmos e Estruturas 1 '
print(palavra)
print(palavra.strip())
print(palavra.strip(' Alg 1 '))
# Método upper e lower
print(palavra.upper())
print(palavra.lower())
# Método replace
doce = 'bananada'
correcao = doce.replace('na', 'ta')
print(doce)
print(correcao)
# Recorrência de padrão
texto = 'Sirius é uma estrela'
padrao = 'estrela' in texto
print(padrao)
# Encontrar padrões
desabafo = 'Passar pano é ruim demais.'
padrao = 'ss'
posicao = desabafo.find(padrao)
posicao = desabafo.index(padrao)
print(posicao)
# Método count(substring, inicio, fim)
string = 'Passar pano é ruim demais.'
caractere = 's'
substring = 'ss'
numCaractere = string.count(caractere)
numSubstring = string.count(substring)
print(numCaractere)
print(numSubstring)

