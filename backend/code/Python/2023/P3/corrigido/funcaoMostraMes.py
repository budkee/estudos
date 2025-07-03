def mostrames(num):
    mes = ''
    if num == 1:
        mes = 'Janeiro'
    elif num == 2:
        mes = 'Fevereiro'
    elif num == 3:
        mes = 'Março'
    elif num == 4:
        mes = 'Abril'
    elif num == 5:
        mes = 'Maio'
    elif num == 6:
        mes = 'Junho'
    elif num == 7:
        mes = 'Julho'
    elif num == 8:
        mes = 'Agosto'
    elif num == 9:
        mes = 'Setembro'
    elif num == 10:
        mes = 'Outubro'
    elif num == 11:
        mes = 'Novembro'
    elif num == 12:
        mes = 'Dezembro'
    else:
        mes = 'Número inválido'
    return mes


num = int(input())
mes = mostrames(num)
print(mes)