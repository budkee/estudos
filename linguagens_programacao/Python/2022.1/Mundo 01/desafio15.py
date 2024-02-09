# Aluguel de um carro sabendo que o carro custa R$60/dia e R$0.15/Km rodado

dias = int(input('Quantos dias de aluguel? '))
km = int(input('Quantos KM rodados? '))

total = (dias * 60) + (km * 0.15)

print('O valor total a ser pago é de R${:.2f}'.format(total))
