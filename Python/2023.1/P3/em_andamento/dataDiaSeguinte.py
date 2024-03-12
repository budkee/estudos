def eh_bissexto(ano):
    """
    Verifica se um ano é bissexto.
    """
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def calcular_dia_seguinte(data):
    """
    Calcula a data do dia seguinte.
    """
    dia, mes, ano = data['dia'], data['mes'], data['ano']

    # Verifica o número de dias em cada mês
    dias_por_mes = {
        1: 31,  # janeiro
        2: 29 if eh_bissexto(ano) else 28,  # fevereiro
        3: 31,  # março
        4: 30,  # abril
        5: 31,  # maio
        6: 30,  # junho
        7: 31,  # julho
        8: 31,  # agosto
        9: 30,  # setembro
        10: 31,  # outubro
        11: 30,  # novembro
        12: 31  # dezembro
    }

    # Verifica se o dia é válido
    if dia < 1 or dia > dias_por_mes[mes]:
        print('Data inválida')
        return

    # Verifica se é o último dia do ano
    if dia == 31 and mes == 12:
        dia_seguinte = 1
        mes_seguinte = 1
        ano_seguinte = ano + 1
    # Verifica se é o último dia do mês
    elif dia == dias_por_mes[mes]:
        dia_seguinte = 1
        mes_seguinte = mes + 1
        ano_seguinte = ano
    else:
        dia_seguinte = dia + 1
        mes_seguinte = mes
        ano_seguinte = ano

    # Cria e retorna a data do dia seguinte
    data_seguinte = {
        'dia': dia_seguinte,
        'mes': mes_seguinte,
        'ano': ano_seguinte
    }

    return data_seguinte


# Leitura da data
dia, mes, ano = map(int, input().split('/'))
data_atual = {
    'dia': dia,
    'mes': mes,
    'ano': ano
}

# Calcula a data do dia seguinte
data_seguinte = calcular_dia_seguinte(data_atual)

# Imprime a data do dia seguinte ou a mensagem 'Data inválida'
if data_seguinte:
    print('{:02d}/{:02d}/{:04d}'.format(
        data_seguinte['dia'], data_seguinte['mes'], data_seguinte['ano']
    ))
