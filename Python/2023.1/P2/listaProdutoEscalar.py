""" Este programa lê uma lista de número float e uma grandeza escalar l e calcula o produto escalar entre eles. """
import numpy as np
# Leia a lista
lista = np.array([float(num) for num in input().split()])
l = float(input())

# Compute o produto escalar
print(lista * l)