print('Conversão de graus Celsius/Fahrenheit')
a = 0
while a != 3:
    print('''    [1] ºF para ºC
    [2] ºC para ºF 
    [3] Fim do programa''')
    a = int(input('Selecione uma das opções: '))

    if a == 1:
        f = float(input('graus em fahrenheit: '))
        c = 5 * ((f - 32) / 9)
        print('{}ºF é o mesmo que {:.2f}ºC.'.format(f, c))

    elif a == 2:
        c = float(input('graus em celsius: '))
        f = 32 + ((c / 5) * 9)
        print('{}ºC é o mesmo que {:.2f}ºF.'.format(c, f))

    elif a == 3:
        print('Até logo!')
    else:
        print('Tente novamente')

    print('''Sensação térmica de acordo com a temperatura (ºC)
     > 40º      Muito Quente
     >= 30º     Quente
     >= 15º     Agradável
     >= 5º      Friozinho
     >= 0º      Frio
     >= -10º    Muito frio
     < -10º     Congelante''')
    print('-----' * 10)
print('Fim do programa')