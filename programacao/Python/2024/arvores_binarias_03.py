from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# Função para percorrer a árvore em nível (BFS)
def level_order_traversal(root):
    if root is None:
        return
    
    # Cria uma fila para manter os nós a serem visitados
    queue = deque([root])
    
    while queue:
        # Remove o nó da frente da fila
        current_node = queue.popleft()
        
        # Processa o nó atual (neste caso, apenas imprime o valor)
        print(current_node.key, end=" ")
        
        # Adiciona os filhos esquerdo e direito à fila, se existirem
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

# Exemplo de uso
if __name__ == "__main__":
    # Criação de uma árvore binária de exemplo
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    # Percorre a árvore em nível
    print("Percurso em nível da árvore binária:")
    level_order_traversal(root)
