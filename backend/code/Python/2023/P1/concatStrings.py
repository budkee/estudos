palavra = 'Algoritmos'
palavra2 = 'Eae!'

# Espaços e alinhamentos
print('{0:11s}{1:s}\n'.format(palavra, palavra2))
print(palavra.rjust(15)) # Ajusta a palavra a 15 espaços para direita
print(palavra.rjust(20,'*')) # Coloca a estrela no lugar do espaço

# Partes de uma string

# Ao contar da esquerda para direita, conte o primeiro caractere a partir do nº 0
print(palavra[0]) # Seleciona o primeiro caractere da string
# Ao contar da direita para esquerda, considere como nº 0 o espaço após o último caractere da string
print(palavra[-1]) # Seleciona o último caractere da string
# Remova o meio da palavra
n = 1
tam = len(palavra)
print(tam)
parte = palavra[2:(tam-n)] # Começa do caractere 2 e termina no caractere anterior ao 9
print(parte)
# Inversão
# print(palavra[0:-1])

