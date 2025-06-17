import numpy as np
import matplotlib.pyplot as plt
from fuzzylogic.classes import Domain, Rule
from fuzzylogic.functions import R, S, triangular, bounded_sigmoid, sigmoid

# Dominios de entrada y salida
suciedad = Domain("Suciedad", low=0, high=100)
superficie = Domain("Superficie", low=0, high=2)
potencia = Domain("Potencia", low=0, high=100)

# Conjunto y pertenencia
suciedad.limpio = S(0, 20)

# Gráfico
plt.figure(figsize=(8, 4))
suciedad.limpio.plot()

plt.title("Conjunto Limpio")
plt.xlabel("Nivel de suciedad")
plt.ylabel("Pertinencia S")
# Define ticks de 10 em 10 para x
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)
plt.legend()

# Conjunto y pertinencia
suciedad.casi_limpio = bounded_sigmoid(10, 30, inverse=True)

plt.figure(figsize=(8, 4))
suciedad.casi_limpio.plot()
plt.title("Conjunto Casi Limpio")
plt.xlabel("Nivel de suciedad")
plt.ylabel("Pertinencia S")
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)

# Conjunto y pertenencia
suciedad.algo_sucio = bounded_sigmoid(25, 55)

# Plota
plt.figure(figsize=(8, 4))
suciedad.algo_sucio.plot()
plt.title("Conjunto Algo Sucio")
plt.xlabel("Nivel de suciedad")
plt.ylabel("Pertinencia R")
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)

# Conjunto y pertenencia
suciedad.sucio = bounded_sigmoid(50, 75)

# Plota
plt.figure(figsize=(8, 4))
suciedad.sucio.plot()
plt.title("Conjunto Sucio")
plt.xlabel("Nivel de suciedad")
plt.ylabel("Pertinencia R")
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)

# Conjunto y pertenencia
suciedad.muy_sucio = R(70, 100)

# Plota
plt.figure(figsize=(8, 4))
suciedad.muy_sucio.plot()
plt.title("Conjunto Muy Sucio")
plt.xlabel("Nivel de suciedad")
plt.ylabel("Pertinencia R")
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)

# Conjuntos 
suciedad.limpio = S(0, 20)
suciedad.casi_limpio = bounded_sigmoid(10, 30, inverse=True)
suciedad.algo_sucio = bounded_sigmoid(25, 55)
suciedad.sucio = bounded_sigmoid(50, 75)
suciedad.muy_sucio = R(70, 100)

# Plota
plt.figure(figsize=(10, 6))
suciedad.limpio.plot()
suciedad.casi_limpio.plot()
suciedad.algo_sucio.plot()
suciedad.sucio.plot()
suciedad.muy_sucio.plot()
plt.title("Conjunto Muy Sucio")
plt.xlabel("Nivel de suciedad")
plt.ylabel("Pertinencia R")
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)

# Define funções de pertinência triangulares
superficie.madera = triangular(-1.0, 1)
superficie.caucho = triangular(0, 2)
superficie.alfombra = triangular(1, 3)

# Plota
plt.figure(figsize=(8, 4))
superficie.madera.plot()
superficie.caucho.plot()
superficie.alfombra.plot()
plt.xlabel("Valor do domínio (0 = madera, 1 = caucho, 2 = alfombra)")
plt.ylabel("Pertinência")
plt.title("Funções de pertinência triangulares")
plt.grid(True)
plt.legend()
plt.ylim(-0.05, 1.05)
plt.show()

potencia.muy_debil = S(0, 20)

# Gráfico
plt.figure(figsize=(8, 4))
potencia.muy_debil.plot()

plt.title("Conjunto Muy Débil ")
plt.xlabel("Nivel de Potencia")
plt.ylabel("Pertinencia S")
# Define ticks de 10 em 10 para x
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)
plt.legend()

potencia.debil = bounded_sigmoid(15, 35, inverse=True)

# Gráfico
plt.figure(figsize=(8, 4))
potencia.debil.plot()

plt.title("Conjunto Débil ")
plt.xlabel("Nivel de Potencia")
plt.ylabel("Pertinencia S")
# Define ticks de 10 em 10 para x
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)
plt.legend()

potencia.normal = bounded_sigmoid(30, 60)

# Gráfico
plt.figure(figsize=(8, 4))
potencia.normal.plot()

plt.title("Conjunto Normal ")
plt.xlabel("Nivel de Potencia")
plt.ylabel("Pertinencia R")
# Define ticks de 10 em 10 para x
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)
plt.legend()

potencia.fuerte = bounded_sigmoid(55, 80)
# Gráfico
plt.figure(figsize=(8, 4))
potencia.fuerte.plot()

plt.title("Conjunto Fuerte ")
plt.xlabel("Nivel de Potencia")
plt.ylabel("Pertinencia R")
# Define ticks de 10 em 10 para x
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)
plt.legend()

potencia.muy_fuerte = R(75, 100)
# Gráfico
plt.figure(figsize=(8, 4))
potencia.muy_fuerte.plot()

plt.title("Conjunto Muy Fuerte ")
plt.xlabel("Nivel de Potencia")
plt.ylabel("Pertinencia R")
# Define ticks de 10 em 10 para x
plt.xticks(np.arange(0, 101, 10))
plt.grid(True)
plt.legend()

R1 = Rule({(suciedad.muy_sucio, superficie.madera): potencia.fuerte})
R2 = Rule({(suciedad.sucio, superficie.madera): potencia.normal})
R3 = Rule({(suciedad.algo_sucio, superficie.madera): potencia.debil})
R4 = Rule({(suciedad.casi_limpio | suciedad.limpio, superficie.madera): potencia.muy_debil})

R5 = Rule({(suciedad.muy_sucio, superficie.caucho): potencia.muy_fuerte})
R6 = Rule({(suciedad.sucio, superficie.caucho): potencia.fuerte})
R7 = Rule({(suciedad.algo_sucio, superficie.caucho): potencia.normal})
R8 = Rule({(suciedad.casi_limpio, superficie.caucho): potencia.debil})
R9 = Rule({(suciedad.limpio, superficie.caucho): potencia.muy_debil})

R10 = Rule({(suciedad.muy_sucio, superficie.alfombra): potencia.muy_fuerte})
R11 = Rule({(suciedad.sucio, superficie.alfombra): potencia.fuerte})
R12 = Rule({(suciedad.casi_limpio | suciedad.algo_sucio, superficie.alfombra): potencia.normal})
R13 = Rule({(suciedad.limpio, superficie.alfombra): potencia.debil})

rules == R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 == sum([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13])

entrada = {suciedad: 65, superficie: 2}
print("Potencia estimada:", rules(entrada))