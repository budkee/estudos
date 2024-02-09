# Conversor de temperaturas


escala = int(input('Qual é a escala de interesse? \n' '[1] Kelvin\n' '[2] Celsius\n' '[3] Fahrenheit\n'
'Resposta: '))


if escala == 1:
    escala2 = int(input('Qual é a escala dada pelo problema?\n' '[1] Fahrenheit \n' '[2] Celsius\n' 'Resposta: '))
    if escala2 == 1:
        fahren = float(input('\nQual é a temperatura em Fahrenheit(F)? '))
        tempK = (fahren - 32)* (5/9) + 273
        print('{:.2f}ºF equivale a {:.2f}ºK'. format(fahren, tempK))
    elif escala2 == 2:
        celcius = float(input('\nQual é a temperatura em Celsius (C)? '))
        tempK = celcius + 273
        print('{:.2f}ºC equivale a {:.2f}ºK'. format(celcius, tempK))

elif escala == 2:
    escala2 = int(input('Qual é a escala dada pelo problema?\n' '[1] Fahrenheit \n' '[2] Kelvin\n' 'Resposta: '))
    if escala2 == 1:
        fahren = float(input('\nQual é a temperatura em Fahrenheit(F)? '))
        tempC = (fahren - 32)/1.8
        print('{:.2f}ºF equivale a {:.2f}ºC'. format(fahren, tempC))
    elif escala2 == 2:
        kelvin = float(input('\nQual é a temperatura em Kelvin(K)? '))
        tempC = kelvin - 273
        print('{:.2f}ºK equivale a {:.2f}ºC'. format(kelvin, tempC))

elif escala == 3:
    escala2 = int(input('Qual é a escala dada pelo problema?\n' '[1] Celsius \n' '[2] Kelvin\n' 'Resposta: '))
    if escala2 == 1:
        celcius = float(input('\nQual é a temperatura em Celsius(C)? '))
        tempF = (celcius * 1.8) + 32
        print('{:.2f}ºC equivale a {:.2f}ºF'. format(celcius, tempF))
    elif escala2 == 2:
        kelvin = float(input('\nQual é a temperatura em Kelvin(K)? '))
        tempF = (kelvin - 273) * 1.8 + 32
        print('{:.2f}ºK equivale a {:.2f}ºC'. format(kelvin, tempF))

print('Fim do programa.')
