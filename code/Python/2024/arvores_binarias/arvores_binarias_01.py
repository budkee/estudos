class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# Função recursiva para calcular o número de nós em cada subárvore
def count_nodes(root):
    # Se o nó for None, a subárvore é vazia, retorna 0
    if root is None:
        return 0
    
    # Conta o número de nós na subárvore esquerda e direita
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    
    # Soma 1 (o próprio nó) com os nós das subárvores esquerda e direita
    root.subtree_size = 1 + left_count + right_count
    
    return root.subtree_size

# Função para percorrer a árvore e imprimir o tamanho das subárvores
def print_subtree_sizes(root):
    if root:
        print(f"Nó {root.key}: Subárvore tem {root.subtree_size} nós")
        print_subtree_sizes(root.left)
        print_subtree_sizes(root.right)

# Exemplo de uso
if __name__ == "__main__":
    # Criação de uma árvore binária de exemplo
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    # Calcula o número de nós em cada subárvore
    count_nodes(root)
    
    # Imprime o número de nós das subárvores
    print_subtree_sizes(root)