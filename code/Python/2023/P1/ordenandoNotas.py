# Programa: ordenanotas00.py
# Programador:
# Data: 22/09/2016
# Este programa lê uma lista com três notas entre 0.0 e 10.0, ordena a
# lista de notas em ordem não decrescente e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# float nota1, nota2, nota3, aux
# pré: para i = {0, 1, 2}:nota[i] | 0.0 <= nota[i] <= 10.0
# Passo 1. Leia as notas
nota1,nota2,nota3 = map(float, input().split())
# Passo 2. Ordene as notas nota1, nota2, nota3
# Passo 2.1. Calcule a menor nota e armazene em nota1
if nota2 < nota1:
   aux = nota1
   nota1 = nota2
   nota2 = aux
if nota3 < nota1:
   aux = nota1
   nota1 = nota3
   nota3 = aux
# Passo 2.2. Calcule a segunda menor nota e armazene em nota2
if nota3 < nota2:
   aux = nota2
   nota2 = nota3
   nota3 = aux
# Passo 3. Imprima as notas ordenadas
print(nota1, nota2, nota3)
# pós: para i = {0,1}:nota[i] | nota[i] <= nota[i+1]
# fim do módulo principal