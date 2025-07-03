# Conversor de moedas

cart = float(input('Quanto reais você tem? '))
cot = float(input('Qual é a cotação do dólar hoje? '))

valor = cart / cot

print('Você tem {:.2f} dólares na carteira.'.format(valor)) 
