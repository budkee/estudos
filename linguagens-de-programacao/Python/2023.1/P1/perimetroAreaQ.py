# Algoritmo: Perímetro e Área de um quadrado
# Programador: Cáceres
# Data: 26/03/2010

# Este programa lê o valor do lado > 0 de um quadrado e calcula e imprime o perímetro e a área do quadrado.

# Formato da entrada: 
# Entre com o valor do lado do quadrado > 0: 5.0

# Formato da saída
# Lado = 5.00
# Perímetro = 20.00
# Área = 25.00' 

# pré: lado > 0

# Descrição das variáveis utilizadas
# lado, perimetro, area: float

# Passo 1. Leia o lado do quadrado
lado = float(input('Entre com o valor do lado do quadrado > 0: '))
# Passo 2. Compute o perímetro e a área do quadrado
# Passo 2.1. Calcule o perímetro do quadrado (refinamento)
perimetro = 4 * lado
# Passo 2.2. Calcule a área do quadrado (refinamento)
area = lado**2
# Passo 3. Imprima o perímetro e a área do quadrado
print('Lado = {0:.2f}'. format(lado))
print('Perimetro = {0:.2f}'. format(perimetro))
print('Área = {0:.2f}'. format(area))

# pós: perimetro == 4*lado and area == lado**2