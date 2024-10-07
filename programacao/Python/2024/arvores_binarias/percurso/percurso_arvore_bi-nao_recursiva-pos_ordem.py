from arvores_binarias import Node

# ------------------- Recursivo -------------------
# def pos_ordem(T):
#     if T is not None:
#         # 2. Percorre a subárvore esquerda
#         pre_ordem(T.esquerda)
#         # 3. Percorre a subárvore direita
#         pre_ordem(T.direita)
#         # 1. Visita o nó (raiz)
#         print(T.valor, end=" ")

# ------------------- Não recursivo -------------------
def pos_ordem_nao_recursivo(T):
    if T is None:
        return
    
    pilha1 = []
    pilha2 = []
    
    pilha1.append(T)
    
    while pilha1:
        nodo = pilha1.pop()
        pilha2.append(nodo)
        
        if nodo.esquerda is not None:
            pilha1.append(nodo.esquerda)
        if nodo.direita is not None:
            pilha1.append(nodo.direita)
    
    while pilha2:
        nodo = pilha2.pop()
        print(nodo.valor, end=" ")

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
    pos_ordem_nao_recursivo(T)

    # # Percorre a árvore em pré-ordem
    # print("Percurso em pré-ordem da árvore binária:")
    # pre_ordem(T)
