# Calculo percentual 01

preco = float(input('Valor do produto: '))
desc = 5/100 * preco
preco_desc = preco - desc

print('Preço com um desconto de 5% fica R${}'.format(preco_desc))