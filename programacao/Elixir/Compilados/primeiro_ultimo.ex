defmodule Lista do
  @doc """

    Implementação de duas funções, onde a primeira retorna o primeiro elemento da lista e a segunda retorna o último elemento da lista, e ambos verificam se a lista está vazia.

  """

  # Retira o primeiro elemento do array
  def primeiro([]), do: nil
  def primeiro(lista), do: hd(lista)

  # Retira o último elemento do array
  def ultimo([]), do: nil
  def ultimo(lista), do: Enum.at(lista, -1)

end

# Teste
primeiro = Lista.primeiro([])
ultimo = Lista.ultimo([2, 4, 3, 2, 55])

IO.puts (
  case primeiro do
    nil -> "Lista vazia"
    resultado -> "O primeiro elemento da lista [2, 4, 3, 2, 55] é " <> Integer.to_string(resultado)
  end)

IO.puts (
  case ultimo do
    nil -> "Lista vazia"
    resultado -> "O último elemento da lista [2, 4, 3, 2, 55] é " <> Integer.to_string(resultado)
  end)
