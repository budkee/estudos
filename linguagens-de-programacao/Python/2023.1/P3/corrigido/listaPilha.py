# Início do módulo principal

# Inicialize as variáveis
tam = int(input())
pilha = []
desempilha = []

# Ler os dados
e = list(map(int, input().split()))

# Empilhar
for i in range(tam):
    pilha.append(e[i])
# print(pilha): tudo certo zté aqui

# Desempilhar
for i in range(tam):
    desempilha.append(pilha.pop())

# Imprime o resultado
print(desempilha)