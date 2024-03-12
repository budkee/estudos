# Sobre: Este programa lê o cateto oposto e adjacente e calcula o perimetro e a área de um triângulo retângulo.
# Programador: SiriusB

# Formato de entrada:
# Leia o valor do cateto oposto: 1
# Leia o valor do cateto adjacente: 1

# Formato de saída:
# Perímetro = 3.41
# Área = 0.50

# Constantes e variáveis
# float: catop, catadj, perimetro, area

# Bibliotecas
import math

# Passo 1: leia o cateto oposto e o cateto adjacente
catop = float(input('Leia o valor do cateto oposto: '))
catadj = float(input('Leia o valor do cateto adjacente: '))
# Passo 2: calcule o perimetro e a área
# Passo 2.1: calcule o perimetro
# Passo 2.1.1: calcule o valor da hipotenusa
hip = math.sqrt((catop)**2 + (catadj)**2)
perimetro = catop + catadj + hip
# Passo 2.2: calcule a area
area = (catop*catadj)/2
# Passo 3: imprima o perimetro e a area
print('Perímetro = {:.2f} \nÁrea = = {:.2f}'.format(perimetro, area))