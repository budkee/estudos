# Programa: palindromo.py
# Programador:
# Data: 03/05/2016
# Este programa lê um número inteiro e computa se o número
# é palíndromo e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# int numero, num, reverso, digito
# str msg

# pré: numero == d[k]d[k-1]...d[1]d[0]

# Passo 1. Leia um número e inicialize as variáveis
# Passo 1.1. Leia um numero
numero = int(input('Leia um número inteiro: '))
# Passo 1.2. Faça uma cópia de numero
num = numero
# Passo 1.3. Inicialize reverso
reverso = 0
# Passo 2. Compute o reverso de num e compare com numero
# Passo 2.1. Enquanto num > 0
while num > 0:
    # Passo 2.1.1. Obtenha o último dígito de num
    digito = num % 10
    # Passo 2.1.2. Inclua dígito em reverso
    reverso = (reverso * 10) + digito
    # Passo 2.1.3. Retire dígito de num
    num = num // 10
# Passo 2.2. Se reverso == numero palíndromo
if numero == reverso:
    msg = 'palíndromo'
# Passo 2.3. Caso contrário, não é palíndromo
else:
    msg = 'não é palíndromo'
# Passo 3. Imprima a mensagem
print(msg)

# pós: ('palíndromo' and d[k]d[k-1]...d[1]d[0] == d[0]d[1]...d[k-1]d[k])
#      or 'não é palíndromo'
# fim do módulo principal
