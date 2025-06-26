from typing import List, Tuple, Dict, Set
import copy

class Predicate:

    """Classe que representa um predicado com nome e argumentos.
    
    Sobre: Um predicado é uma função que pode ser unificada com outros predicados para inferir novos fatos ou regras.
    """

    def __init__(self, name: str, args: Tuple[str, ...]):
        self.name = name
        self.args = args  # ex: ("x", "y")

    def __repr__(self):
        return f"{self.name}({', '.join(self.args)})"

    def substitute(self, subs: Dict[str, str]):
        new_args = tuple(subs.get(arg, arg) for arg in self.args)
        return Predicate(self.name, new_args)

    def is_variable(self, x):
        return x[0].islower()

    def unify(self, other: "Predicate") -> Dict[str, str] or None:
        if self.name != other.name or len(self.args) != len(other.args):
            return None
        subs = {}
        for a1, a2 in zip(self.args, other.args):
            if a1 == a2:
                continue
            if self.is_variable(a1):
                subs[a1] = a2
            elif self.is_variable(a2):
                subs[a2] = a1
            else:
                return None
        return subs

    def __eq__(self, other):
        return isinstance(other, Predicate) and self.name == other.name and self.args == other.args

    def __hash__(self):
        return hash((self.name, self.args))



# ========= Forward Chaining =========
def forward_chaining(facts: Set[Predicate], rules: List[Tuple[List[Predicate], Predicate]]) -> Set[Predicate]:

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

            # Encontra todos os fatos que correspondem ao primeiro predicado das premissas
            matches = [f for f in inferred if f.name == premises[0].name]
            for fact in matches:
                subs = premises[0].unify(fact)
                if subs is None:
                    continue
                rest = [p.substitute(subs) for p in premises[1:]]
                if all(any(p.unify(f) is not None for f in inferred) for p in rest):
                    new_conclusion = conclusion.substitute(subs)
                    if new_conclusion not in inferred:
                        inferred.add(new_conclusion)
                        added = True
    return inferred

# ========= Backward Chaining =========
def backward_chaining(goal: Predicate, facts: Set[Predicate], rules: List[Tuple[List[Predicate], Predicate]], visited=None) -> bool:
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

    if any(goal.unify(f) is not None for f in facts):
        return True

    if str(goal) in visited:
        return False
    visited.add(str(goal))  # evitar ciclos

    for premises, conclusion in rules:
        subs = conclusion.unify(goal)
        if subs is None:
            continue
        grounded_premises = [p.substitute(subs) for p in premises]
        if all(backward_chaining(p, facts, rules, visited) for p in grounded_premises):
            return True
    return False


# ========= Testando as funções =========
if __name__ == "__main__":
    
    # Fatos
    facts = {
        Predicate("Pai", ("joao", "maria")),
        Predicate("Pai", ("maria", "ana"))
    }

    # Regras: Pai(x, y) ∧ Pai(y, z) → Avô(x, z)
    rules = [
        ([Predicate("Pai", ("x", "y"))], Predicate("Ancestral", ("x", "y"))),
        ([Predicate("Pai", ("x", "y")), Predicate("Pai", ("y", "z"))], Predicate("Ancestral", ("x", "z")))
    ]

    # Encadeamento para frente
    res = forward_chaining(facts, rules)
    print("Fatos inferidos:", res)

    # Encadeamento para trás
    goal = Predicate("Ancestral", ("joao", "ana"))
    print(f"Pode-se inferir {goal}? ->", backward_chaining(goal, facts, rules))

