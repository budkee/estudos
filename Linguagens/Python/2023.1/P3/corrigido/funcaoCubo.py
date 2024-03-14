
def cubo(num):
    valor = num**3
    return valor


# Inicio do modulo principal
num = float(input())
result = cubo(num)
print('{0:.2f}'.format(result))