def f(x):
    y = x ** 3
    return y

def derivada(x):
    y = 3 * (x ** 2)
    return y

def deriv_lim(x, delta_x):
    y = (f(x + delta_x) - f(x)) / delta_x
    return y

x = 0.2
delta_x = 0.001

# Letra a ("valor experimental")
a = derivada(x)

# Letra b ("valor real")
b = deriv_lim(x, delta_x)

# Erro relativo será o erro absoluto entre b(valor real) e a(valor experimental) dividido pelo b(valor real)
erro_abs = b - a
erro_rel = erro_abs / b

print('x = {}        derivada(x) = {} \n'
      'x = {}        deriv_lim(x, delta_x) = {}       Erro Relativo = {:2f}\n'.format(x, a, x, b, erro_rel))
