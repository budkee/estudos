# Programa: sucoscerrado.py
# Programador:
# Data:

# Este programa gera aleatoriamente uma amostra de sucos e a
# avaliação dos consumidores relativa aos sucos consumidos.
# O programa computa o número de sucos comercializados e
# quais sucos foram mais apreciados e quais sucos foram menos
# apreciados.

# início do módulo principal

# declaração das bibliotecas utilizadas
import random

# descrição das variáveis utilizadas
# list sucos[{}]
# list chaves, tipos
# list amostra, avalia
# list lvendas, lavabom, lavaruim
# list lmais, lbom. lruim
# int maxvendas, maxbom, maxruim

# pré: amostra[0] .. amostra[999] (geradas aleatoriamente)

# Passo 1. Defina e inicialize as estruturas e leia os dados
# Passo 1.1. Defina a lista das chaves
chaves = ['nome', 'vendas', 'avalia']

# Passo 1.2. Inicialize a lista dos tipos de suco
tipos = ['araticum', 'butia', 'cagaita', 'caja', 'guavira', 'inga', 'jabuticaba',
         'jaracatia', 'mangaba', 'pitanga', 'pitomba', 'tucum']

# Passo 1.3. Inicialize a lista de sucos
sucos = [dict.fromkeys(chaves) for _ in range(len(tipos))]

# Passo 1.4. Inicialize a lista dos sucos
for i in range(len(tipos)):
    sucos[i]['nome'] = tipos[i]
    sucos[i]['vendas'] = 0
    sucos[i]['avalia'] = [0, 0, 0]

# Passo 1.5. Gere uma entrada (amostra) aleatória
random.seed()
avalia = ['bom', 'medio', 'ruim']
amostra = [[random.choice(tipos), random.choice(avalia)] for i in range(1000)]

# Passo 2. Compute a quantidade de sucos vendidos e a avaliação
# Passo 2.1. Compute a tabela de vendas
for i in range(len(amostra)):  # tamanho da entrada
    for j in range(len(tipos)):  # tipos de sucos
        if amostra[i][0] == sucos[j]['nome']:
            sucos[j]['vendas'] += 1
            if amostra[i][1] == 'bom':
                sucos[j]['avalia'][0] += 1
            elif amostra[i][1] == 'medio':
                sucos[j]['avalia'][1] += 1
            elif amostra[i][1] == 'ruim':
                sucos[j]['avalia'][2] += 1

# Passo 2.2. Compute a quantidade dos sucos mais vendidos
maxvendas = max(sucos[i]['vendas'] for i in range(len(tipos)))

# Passo 2.3. Compute a quantidade dos sucos mais bem avaliados
maxbom = max(sucos[i]['avalia'][0] for i in range(len(tipos)))

# Passo 2.4. Compute a quantidade dos sucos mais mal avaliados
maxruim = max(sucos[i]['avalia'][2] for i in range(len(tipos)))

# Passo 2.5. Compute a lista dos sucos mais vendidos
lmais = [d['nome'] for d in sucos if d['vendas'] == maxvendas]

# Passo 2.6. Compute a lista dos sucos mais bem avaliados
lbom = [d['nome'] for d in sucos if d['avalia'][0] == maxbom]

# Passo 2.7. Compute a lista dos sucos mais mal avaliados
lruim = [d['nome'] for d in sucos if d['avalia'][2] == maxruim]

# Passo 3. Imprima os resultados
print('Sucos mais vendidos:', lmais, maxvendas)
print('Sucos mais apreciados:', lbom, maxbom)
print('Sucos menos apreciados:', lruim, maxruim)

# pós: [lmais] maxvendas [lbom] maxbon [lruim] maxruim
# fim do módulo principal
