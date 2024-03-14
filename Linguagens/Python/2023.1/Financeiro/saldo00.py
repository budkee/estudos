# Data: 06/07/23
# Nome do programa: saldo00.py
# Programadore: siriusB

# Este programa tem como objetivo (1) receber o valor de entrada, (2) receber o valor a
# ser guardado para o início do mês e (3) receber o valor a ser pago na data de
# entrada. Em seguida, ele deverá retornar (4) o saldo disponível para o próximo mês.

# Valores de teste
# Receita: R$3000
# Caixinha: R$(593 + 280 + 85 + 84,90)
# Pagamento: R$(406,96 + 1738,52)
# Limite da fatura do próximo mês: R$

# Bibliotecas
import pandas as pd

# Declarações
chaves_caixinha = ['Aluguel', 'CondominioAgua', 'Luz', 'Internet', 'Alimentacao']
tam = len(chaves_caixinha)
caixinha = dict.fromkeys(chaves_caixinha)
dados = []
print(caixinha)
limite = 0.0 # Quanto eu posso gastar via crédito?
saldo = 0.0 # quanto eu posso gastar à vista?

# Entradas
receita = float(input('Quanto de receita caiu na conta este mêS?: '))

print('Quanto deverá ir para caixinha?\n')
for i in range(tam):
    dados = input('{0}: R$ '.format(chaves_caixinha[i]))
    caixinha[i]['Aluguel'].append(dados[0])
    print(caixinha)
    caixinha[i]['CondominioAgua'] = dados[1]
    caixinha[i]['Luz'] = dados[2]
    caixinha[i]['Internet'] = dados[3]
    caixinha[i]['Alimentacao'] = dados[4]


print(caixinha)

#pagamento = float(input('Quanto deve ser descontado na data de hoje?: '))

# Cálculos



# Saída
#print('Limite para o próximo mês: {}'.format(limite))