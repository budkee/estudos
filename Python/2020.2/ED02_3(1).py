print('Valor do salário a ser pago a um funcionário.')

while True:
    s = input('Qual o salário/hora?: ')
    h = input('Quantas horas de trabalho?: ')
    try:
        s = float(s)
        h = float(h)
        if h <= 40:
            sp = h * s
            print('O funcionário que trabalhou {} horas vai receber um salário de R${:.2f}'.format(h, sp))
            break
        else:
            sp = s * 40
            sp = sp + (h - 40) * (s * 1.5)
            print('O salário com reajuste de 50% será no valor de R${:.2f}'.format(sp))
            break
    except ValueError:
        print('Eu só leio algarismos numéricos, me ajuda a te ajudar.')
    print("-----" * 15)


