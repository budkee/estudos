from arvores_binarias import Node

# ------------------- Recursivo -------------------
# def pre_ordem(T):
#     if T is not None:
#         # 1. Visita o nó (raiz)
#         print(T.valor, end=" ")
#         # 2. Percorre a subárvore esquerda
#         pre_ordem(T.esquerda)
#         # 3. Percorre a subárvore direita
#         pre_ordem(T.direita)

# ------------------- Não recursivo -------------------
def pre_ordem_nao_recursivo(T):
    if T is None:
        return
    
    # Usamos uma pilha para armazenar os nós
    pilha = []
    # Inicialmente, empilhamos a raiz
    pilha.append(T)
    
    while pilha:
        # Desempilha um nó e processa seu valor
        nodo = pilha.pop()
        print(nodo.valor, end=" ")
        
        # Empilha a subárvore direita (para ser processada depois)
        if nodo.direita is not None:
            pilha.append(nodo.direita)
        
        # Empilha a subárvore esquerda (para ser processada antes)
        if nodo.esquerda is not None:
            pilha.append(nodo.esquerda)


# Exemplo de uso
if __name__ == "__main__":
    # Criação de uma árvore binária de exemplo
    # Raiz | Nível 0
    T = Node('A')
    # Subarvore esquerda | Nível 1
    T.esquerda = Node('B')
    # Nível 2
    T.esquerda.esquerda = Node('C')
    T.esquerda.direita = Node('D')
    
    # Nível 3
    T.esquerda.esquerda.esquerda = Node('F')
    T.esquerda.esquerda.direita = Node('H')
    T.esquerda.direita.esquerda = Node('L')
    T.esquerda.direita.direita = Node('M')
    
    # Subarvore direita | Nível 1
    T.direita = Node('P')
    # Nível 2
    T.direita.esquerda = Node('N')
    T.direita.direita = Node('I')
    # Nível 3
    T.direita.esquerda.esquerda = Node('E')
    T.direita.esquerda.direita = Node('G')
        
    # Percorre a árvore em pré-ordem
    print("Percurso em pré-ordem não recursivo da árvore binária:")
    pre_ordem_nao_recursivo(T)

    # # Percorre a árvore em pré-ordem
    # print("Percurso em pré-ordem da árvore binária:")
    # pre_ordem(T)
