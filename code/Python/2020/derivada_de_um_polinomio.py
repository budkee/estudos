print('Quais sao os coeficientes do seu polinomio?')
a = int(input("Coeficiente a: "))
b = int(input("Coeficiente b: "))
c = int(input("Coeficiente c: "))

print('Quais são os expoentes do seu polinomio?')
n1 = int(input("Expoente {}x: ".format(a)))
n2 = int(input("Expoente {}x: ".format(b)))
n3 = int(input("Expoente {}x: ".format(c)))


def f(x):
    y = a * ((x) ** n1) + b * ((x) ** n2) + c * ((x) ** n3)
    return y

def deriv(x,h):
    y = (f(x + h) - f(x)) / h
    return y


print('A sua função é f(x) = {}.xˆ{} + {}.xˆ{} '.format(a, n1, b, n2, c, n3))
print('A derivada dessa função é f(x) = {}.xˆ{} + {}.xˆ{} '.format(n1 * a, n1 - 1, n2 * b, n2 - 1))
x = int(input('Insira um valor para x = '))
h = 0.00001
print('O valor numérico da sua derivada com h tendendo a 0 é = {:.4f}'.format(deriv(x, h)))
