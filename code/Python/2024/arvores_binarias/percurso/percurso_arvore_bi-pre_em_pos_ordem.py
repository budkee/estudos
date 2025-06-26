from arvores_binarias import Node

def pre_ordem(T):
    if T is not None:
        # 1. Visita o nó (raiz)
        print(T.valor, end=" ")
        # 2. Percorre a subárvore esquerda
        pre_ordem(T.esquerda)
        # 3. Percorre a subárvore direita
        pre_ordem(T.direita)

def em_ordem(T):
    if T is not None:
        # 1. Percorre a subárvore esquerda
        em_ordem(T.esquerda)
        # 2. Visita o nó (raiz)
        print(T.valor, end=" ")
        # 3. Percorre a subárvore direita
        em_ordem(T.direita)

def pos_ordem(T):
    if T is not None:
        # 1. Percorre a subárvore esquerda
        pos_ordem(T.esquerda)
        # 2. Percorre a subárvore direita
        pos_ordem(T.direita)
        # 3. Visita o nó (raiz)
        print(T.valor, end=" ")


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
    print("Percurso em pré-ordem da árvore binária:")
    pre_ordem(T)
    
    # Percorre a árvore em ordem simétrica
    print("\nPercurso em ordem simétrica da árvore binária:")
    em_ordem(T)
    
    # Percorre a árvore em pós-ordem
    print("\nPercurso em pós-ordem da árvore binária:")
    pos_ordem(T)