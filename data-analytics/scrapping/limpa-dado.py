"""
    Este programa realiza a limpeza de uma linha contendo os valores de um arquivo csv, com as colunas separadas por uma vírgula.

"""
linha = '"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40'

# Separa os valores
linha = linha.split(',')
print(linha)
# Remove os caracteres indesejáveis
for valor in range(len(linha)):
    linha = linha[valor].replace('"', '')
print(linha)

    

