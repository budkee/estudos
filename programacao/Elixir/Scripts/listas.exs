@doc """
  Para ler as declarações do programa, a linguagem considera que o objeto "lista" é equivalente ao objeto [1, 2, 3, 4, 5], por exemplo.
"""

# Criando uma lista simples
lista = [1, 2, 3, 4, 5]

# Usando a função list/1
outra_lista = List.list("hello")

# Usando a sintaxe de |
lista_concatenada = [1, 2, 3 | [4, 5, 6]]

# Usando a função [] com |
lista_construida = [1 | [2 | [3 | []]]]

# Exibição no console
IO.inspect(lista)
IO.inspect(outra_lista)
IO.inspect(lista_concatenada)
IO.inspect(lista_construida)
