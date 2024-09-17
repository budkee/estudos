from arvores_binarias import Node

# ------------------- Recursivo -------------------
# def em_ordem(T):
#     if T is not None:
#         # 2. Percorre a subárvore esquerda
#         pre_ordem(T.esquerda)
#         # 1. Visita o nó (raiz)
#         print(T.valor, end=" ")
#         # 3. Percorre a subárvore direita
#         pre_ordem(T.direita)

# ------------------- Não recursivo -------------------
def em_ordem_nao_recursivo(T):
    pilha = []
    atual = T
    
    while pilha or atual:
        # Desce até o nó mais à esquerda
        while atual:
            pilha.append(atual)
            atual = atual.esquerda
        
        # Processa o nó
        atual = pilha.pop()
        print(atual.valor, end=" ")
        
        # Passa para a subárvore direita
        atual = atual.direita


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
    em_ordem_nao_recursivo(T)
