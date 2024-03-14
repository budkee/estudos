def p_ou_i(x):
    if x % 2 == 0:
        x = print('Par')
        return x
    else:
        x = print('Ímpar')
    return x


x = int(input('Insira um número: '))
p_ou_i(x)


