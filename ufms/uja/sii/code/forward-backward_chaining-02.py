from kanren import Relation, facts, run, var, conde, transitive
from kanren.core import lall

# === Declarando relações ===
pai = Relation()

# Fatos (Pai)
facts(pai, 
      ("joao", "maria"),
      ("maria", "ana")
)

# === Variáveis lógicas ===
x, y, z = var(), var(), var()

# === Regra 1: Pai(x, y) → Ancestral(x, y)
def ancestral(x, y):
    return conde([pai(x, y)],
                 [pai(x, z), ancestral(z, y)])

# === Consultas (encadeamento para trás)
# Quem são os ancestrais de 'ana'?
res1 = run(5, x, ancestral(x, 'ana'))
print("Ancestrais de ana:", res1)

# Quem são os descendentes de 'joao'?
res2 = run(5, y, ancestral('joao', y))
print("Descendentes de joao:", res2)

# João é ancestral de Ana?
res3 = run(1, x, lall(ancestral('joao', 'ana')))
print("João é ancestral de Ana?", bool(res3))