# Fatos são strings simples
facts = {"A", "B"}

# Regras são tuplas: (premissas, conclusão)
rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"C", "D"}, "E")
]

# ========= Forward Chaining =========
def forward_chaining(facts, rules):

    """Realiza a inferência por encadeamento para frente.

    Args:
        facts (set): Os fatos conhecidos.
        rules (list): As regras de inferência.

    Returns:
        set: Um conjunto de fatos inferidos a partir dos fatos e regras fornecidos.
    """

    # Inferências conhecidas
    inferred = set(facts)
    added = True
    
    while added:
        # Se não houver novas inferências, sai do loop
        added = False
        for premises, conclusion in rules:
            if premises.issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                added = True
    return inferred

# ========= Backward Chaining =========
def backward_chaining(goal, facts, rules, visited=None):
    """Verifica se um objetivo pode ser alcançado a partir de fatos e regras fornecidos.

    Args:
        goal (str): O objetivo a ser alcançado.
        facts (set): Os fatos conhecidos.
        rules (list): As regras de inferência.
        visited (set, optional): Fatos já visitados. Defaults to None.

    Returns:
        bool: True se o objetivo pode ser alcançado, False caso contrário.
    """
    if visited is None:
        visited = set()

    if goal in facts:
        return True

    if goal in visited:
        return False  # evitar ciclos

    visited.add(goal)

    for premises, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(p, facts, rules, visited) for p in premises):
                return True
    return False


# ========= Testando as funções =========
if __name__ == "__main__":
    
    # Testando Forward Chaining
    inferred_facts = forward_chaining(facts, rules)
    print("Fatos inferidos (Forward Chaining):", inferred_facts)

    # Testando Backward Chaining
    goal = "E"
    can_achieve_goal = backward_chaining(goal, facts, rules)
    print(f"É possível alcançar o objetivo '{goal}' (Backward Chaining):", can_achieve_goal)
