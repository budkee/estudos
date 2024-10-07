from arvores_binarias import Node

def busca_valor(T, x):
    # Se o nó atual for None, retornamos False (árvore vazia ou final do ramo)
    if T is None:
        return False
    
    # Se o valor do nó atual for igual a x, retornamos True
    if T.valor == x:
        return True
    
    # Caso contrário, continuamos a busca na subárvore esquerda e direita
    return busca_valor(T.esquerda, x) or busca_valor(T.direita, x)

# Exemplo de uso:
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
        
    # Testando o algoritmo para buscar um valor
    valor_a_procurar = input('Digite uma letra de A a P para buscar na árvore: ').upper()
    
    if busca_valor(T, valor_a_procurar):
        print(f"O valor '{valor_a_procurar}' está presente na árvore.")
    else:
        print(f"O valor '{valor_a_procurar}' não foi encontrado na árvore.")