# Programa: publicidade.py

# Este algoritmo lê o número de armários vendidos por mês,
# o lucro por armário e os custos de publicidade e operacional da empresa.
# Calcula quanto deve ser investido em publicidade até que o lucro da
# empresa comece a diminuir.

# início do módulo principal

# descrição das variáveis utilizadas
# int numArmarios, numNArmarios
# float lucroArmario, lucro, lucroN
# float custoOperacional, custoPublicidade, custoNPublicidade

# pré: numArmarios lucroArmario custoPublididade custoOperacional

# Passo 1. Leia a entrada
# Passo 1.1. Leia o número de armários vendidos
numArmarios = int(input())
# Passo 1.2. Leia o lucro bruto por armário
lucroArmario = float(input())
# Passo 1.3. Leia o custo da publicidade
custoPublicidade = float(input())
# Passo 1.4. Leia o custo operacional
custoOperacional = float(input())
# Passo 2. Calcule o lucro da empresa
# Passo 2.1. Calcule o lucro atual da empresa
lucro = numArmarios * lucroArmario - custoPublicidade - custoOperacional
# Passo 2.2. Calcule o novo lucro com o aumento de publicidade
# Passo 2.2.1. Calcule o novo custo de publicidade
custoNPublicidade = 2.0*custoPublicidade
# Passo 2.2.2. Calcule o novo número de armários vendidos
numNArmarios = (120*numArmarios)/100
# Passo 2.2.3. Calcule o novo lucro com o aumento de publicidade
lucroN = numNArmarios*lucroArmario - custoNPublicidade - custoOperacional
# Passo 2.3. Compute o investimento máximo em publicidade
while lucroN > lucro:
# Passo 2.3.1. Atualize as vendas de armários
   numArmarios = numNArmarios
# Passo 2.3.2. Atualize o custo da publicidade
   custoPublicidade = custoNPublicidade
# Passo 2.3.3. Atualize o lucro
   lucro = lucroN
# Passo 2.3.4. Calcule o novo custo da publicidade
   custoNPublicidade = 2.0*custoPublicidade
# Passo 2.3.5. Calcule o novo número de armários vendidos
   numNArmarios = (120*numArmarios)/100
# Passo 2.3.6. Calcule o novo lucro com o aumento da publicidade
   lucroN = numNArmarios*lucroArmario - custoNPublicidade - custoOperacional
# fim while
# Passo 3. Imprima os resultados
# Passo 3.1. Imprima o número de armários vendidos
print(numArmarios )
# Passo 3.2. Imprima o Custo da Publicidade
print(custoPublicidade )
# Passo 5.3. Imprima o lucro
print(lucro )

# pós: numArmarios, custoPublicidade, lucro
# fim módulo principal