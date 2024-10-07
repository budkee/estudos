from arvores_binarias import Node

def em_ordem(T):
    if T is not None:
        # 1. Percorre a subárvore esquerda
        em_ordem(T.esquerda)
        # Verifica se é folha (não tem filhos)
        if T.esquerda is None and T.direita is None:
            print(T.valor, end=" ")
        # 3. Percorre a subárvore direita
        em_ordem(T.direita)


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
        
    
    # Percorre a árvore em ordem simétrica
    print("\nImprime as folhas da árvore binária:")
    em_ordem(T)
    
