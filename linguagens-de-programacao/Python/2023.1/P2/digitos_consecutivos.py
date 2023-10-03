# Programa: consecutivos.py
# Programador:
# Data: 03/05/2016
# Este programa lê um número inteiro e computa se o número
# possui dois dígitos consecutivos iguais e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# int numero, digito, diganterior
# str msg

# pré: numero

# Passo 1. Leia um número e inicialize as variáveis
# Passo 1.1. Leia um numero
numero = int(input())
# Passo 1.2. Inicialize a variável msg com 'não'
msg = 'não'
# Passo 1.3. Inicialize as variáveis diganterior com um valor dummy
diganterior = 10  # inicializa diganterior com um dado fictício
# Passo 2. Decomponha o numero enquanto numero > 0
while numero > 0:
    # Passo 2.1. Calcule o digito menos significativo
    digito = numero % 10
    # Passo 2.2. Se digito é igual a digito anterior
    if diganterior == digito:
        # Passo 2.2.1. Atribua 'sim' para a msg
        msg = 'sim'
        numero = 0  # finaliza a verificação
    # Passo 2.3. Caso contrário
    else:
        # Passo 2.3.1. Armazene o digito em digito anterior
        diganterior = digito
        # Passo 2.3.2. Retire o digito menos significativo de numero
        numero = numero // 10
# Passo 3. Imprima a mensagem
print(msg)

# pós: ('sim' and d[i] == d[i-1]) or 'não'
# fim do módulo principal
