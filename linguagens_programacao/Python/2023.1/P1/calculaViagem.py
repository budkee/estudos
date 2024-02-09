# -*- coding: utf-8 -*-
# Programa: viagem.py
# Programador:
# Data: 04/05/2016
# Este programa lê a distância em quilometros da sede local da representação
# de uma organização ao local de um evento que reune todos os representantes
# da organização. Baseado na distância entre a sede local e o local do
# evento, o programa calcula a ajuda de custo para o representante.
# início do módulo principal
# descrição das variáveis utilizadas
# int   sede, distancia
# float ajudaCusto

# pré: sede distancia

# Passo 1. Leia o numero da sede local e a distancia1
sede = int(input())
distancia = int(input())
# Passo 2. Calcule a ajuda de custo
if distancia <= 500:
    ajudaCusto = distancia * 0.15
elif distancia <= 1000:
    ajudaCusto = 75 + (distancia - 500) * 0.12
elif distancia <= 1500:
    ajudaCusto = 135 + (distancia - 1000) * 0.10
elif distancia <= 2000:
    ajudaCusto = 185 + (distancia - 1500) * 0.08
elif distancia <= 3000:
    ajudaCusto = 225 + (distancia - 2000) * 0.06
elif distancia > 3000:
    ajudaCusto = 285 + (distancia - 3000) * 0.05
# Passo 3. Imprima a ajuda de custo do representante i
print('Sede: {0} - R${1:8.2f}'.format(sede, ajudaCusto))


# pós: (sede and ajudaCusto == (distancia <= 500 and 0.15 * distancia) or
#      (distancia <=1000 and 75.00 + 0.12 * (distancia-500))
#      or (distancia <= 1500 and 135.00 + 0.10 * (distancia-1000)) or
#      (distancia <= 2000 and 185.00 + 0.08 * (distancia-1500)) or
#      (distancia <= 3000 and 225.00 + 0.06 * (distancia-2000)) or
#      285.00 + 0.05 * (distancia-3000))
# fim do módulo principal
