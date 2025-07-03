# Programa: somadig.py
# Este programa lê um número inteiro de pelo menos três dígitos, calcula
# a soma dos três dígitos menos significativos e imprime a soma.
# descrição das variáveis utilizadas
# int numero, dig0, dig1, dig2, soma
# pré: numero == dk..d1d0 and 0 <= di <= 9
# Passo 1. Leia o numero inteiro de pelo menos 3 dígitos
numero = int(input())
# Passo 2. Calcule a soma dos três dígitos menos significativos
# Passo 2.1. Calcule o digito menos significativo
dig0 = numero % 10
# Passo 2.2. Calcule o segundo digito menos significativo
dig1 = (numero // 10) % 10
# Passo 2.3. Calcule o terceiro digito menos significativo
dig2 = ((numero // 10) // 10) % 10
# Passo 2.4. Calcule a soma dos três dígitos
soma = dig2 + dig1 + dig0
# Passo 3. Imprima a soma
print(soma)
# pós: soma == d2 + d1 + d0
# fim do módulo principal