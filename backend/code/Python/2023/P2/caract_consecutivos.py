# Programa: consecutivosstr.py
# Programador:
# Data: 
# Este programa lê uma palavra formada por caracteres visíveis e computa
# se a palavra possui dois caracteres consecutivos iguais e imprime o
# resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# str palavra, caractere, temp, msg

# pré: palavra

# Passo 1. Leia uma palavra e inicialize as variáveis
# Passo 1.1. Leia uma palavra com caracteres visíveis
palavra = str(input())
# Passo 1.2. Inicialize a variável msg com 'não'
msg = 'não'
# Passo 1.3. Inicialize a variável charanterior com um valor ''
charanterior = ''  # inicializa charanterior com um dado vazio
# Passo 2. Para cada caractere da palavra
for caractere in palavra:
    # Passo 2.1. Se o i-ésimo caractere for igual ao i-1-caractere
    if caractere == charanterior:
        # Passo 2.1.1. Atribua 'sim' para a msg e sai do laço
        msg = 'sim'
        break  # sai do laço for
    # Passo 2.2. Caso contrário
    else:
        # Passo 2.2.1. Armazene o caractere i em caractere anterior
        charanterior = caractere
    # Passo 3. Imprima a mensagem
print(msg)

# pós: ('sim' and c[i-1] == c[i]) or 'não'
# fim do módulo principal
