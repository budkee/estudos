import random, string

num = int(input())
semente = random.seed(int(input()))

alfabetoCompleto = string.ascii_letters + string.digits + string.punctuation 
senha = ''
char = ''

""" Usando o módulo choice() e shuffle() """

i = 0
# Gere num-3 caracteres aleatórios:
while i <= num-4:
    char = random.choice(alfabetoCompleto)
    senha += char
    i += 1


# Adicione os caracteres obrigatórios
# 1 Letra maiúscula:
char = random.choice(string.ascii_uppercase)
senha += char

# 1 Dígito:
char = random.choice(string.digits)
senha += char

# 1 Símbolo de pontuação
char = random.choice(string.punctuation)
senha += char


# Transforme a string em uma lista
listaSenha = list(senha)

# Emabaralhe os caracteres da lista:
random.shuffle(listaSenha)

# Transforme a lista em string:
senha = ''
for char in listaSenha:
    senha += char

print(senha) 

""" Usando módulo sample(), choice() e shuffle() 

# Gere os num-3 caracteres aleatórios
listaSenha = random.sample(alfabetoCompleto, num-3)
print(listaSenha)
# Adicione os caracteres obrigatórios
# 1 Letra maiúscula:
char = random.choice(string.ascii_uppercase)
listaSenha.append(char)

# 1 Dígito:
char = random.choice(string.digits)
listaSenha.append(char)

# 1 Símbolo de pontuação
char = random.choice(string.punctuation)
listaSenha.append(char)

# Embaralhe a lista
random.shuffle(listaSenha)

# Transforme a lista em string:
senha = ''
for char in listaSenha:
    senha += char

print(senha) """