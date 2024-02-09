# Leia o texto e a palavra de interesse
texto = str(input())
palavra = str(input())

# Leia o tamanho do texto e da palavra
tam1 = len(texto)
tam2 = len(palavra)

# Inicialize os indices de busca
i = 0 
j = 0

# Compare os tam2 caracteres de palavra em texto
while i < tam1 and j < tam2: 
   if texto[i] == palavra[j]:
      i = i + 1 # vá para o próximo caractere em texto
      j = j + 1 # vá para o próximo caractere em palavra
   else: 
      i = i - j + 1 # vá ao caractere seguinte do início comparação
      j = 0 # vá para o caractere inicial em palavra

# Verifique se o índice de busca j(palavra) corresponde ao tamanho da palavra
if j == tam2:
    msg = 'sim'
else:
    msg = 'não'

# Imprima o resultado
print(msg)