Programa: variancia.py
# Programador:
# Data: 23/08/2016
# Este programa lê quatro notas de provas variando de 0.0 a 10.0, (o usuário entra com as notas dentro dos limites), calcula a média a variância e o desvio padrão das quatro notas das provas. Os resultados são impressos usando um formato dado de saída.

# declaração dos módulos utilizados
import math

# início do módulo principal
# descrição das variáveis utilizadas
# float prova1, prova2, prova3, prova4
# float somaprovas, mediaprovas, somaquadrados
# float desviopadrao, variancia

# pré: prova1, prova2, prova3, prova4

# Passo 1. Leia as notas
prova1, prova2, prova3, prova4 = map(float, input().split())
# Passo 2. Calcule a média, variância e desvio padrão
# Passo 2.1. Calcule a soma das notas das provas
somaprovas = prova1 + prova2 + prova3 + prova4
# Passo 2.2. Calcule a média das provas
mediaprovas = somaprovas/4.0
# Passo 2.3. Calcule a soma dos quadrados das notas provas
somaquadrado = prova1**2 + prova2**2 + prova3**2 + prova4**2
# Passo 2.4. Calcule a variância
variancia = somaquadrado/4.0 - (somaprovas**2)/(4.0**2)
# Passo 2.5. Calcule o desvio padrão
desviopadrao = math.sqrt(variancia)
# Passo 3. Imprima a média, a variância e o desvio padrão
print('Primeira Prova    {0:4.1f}'.format(prova1))
print('Segunda Prova     {0:4.1f}'.format(prova2))
print('Terceira Prova    {0:4.1f}'.format(prova3))
print('Quarta Prova      {0:4.1f}'.format(prova4))
print('Média das Provas  {0:5.2f}'.format(mediaprovas))
print('Variância         {0:5.2f}'.format(variancia))
print('Desvio Padrão     {0:5.2f}'.format(desviopadrao))
# pós: media == (Soma i em {1,2,3,4}: prova[i])/4.0 and variancia == ((1/n)*(Soma i em {1,2,3,4}: (prova[i])**2) - (1/n**2)*(Soma i em {1,2,3,4}: prova[i])**2)) and desviopadrao == sqrt(variancia)
# fim do módulo principal