class Node:
    def __init__(self, valor):
        self.esquerda = None
        self.direita = None
        self.valor = valor

# Função recursiva para calcular o número total de nós da árvore
def count_total_nodes(root):
    # Se o nó for None, não há nós, retorna 0
    if root is None:
        return 0
    
    # Contar o próprio nó (1) mais o número de nós na subárvore esquerda e direita
    return 1 + count_total_nodes(root.left) + count_total_nodes(root.right)

# Exemplo de uso
if __name__ == "__main__":
    # Criação de uma árvore binária de exemplo
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    # Calcula o número total de nós na árvore
    total_nodes = count_total_nodes(root)
    
    # Exibe o número total de nós
    print(f"Número total de nós na árvore: {total_nodes}")