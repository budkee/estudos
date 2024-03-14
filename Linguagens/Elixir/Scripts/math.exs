# Módulo
defmodule TDSOFT do

  def soma(a, b), do: a + b
  # Cálculo de fatorial
  def fatorial(0), do: 1
  def fatorial(n), do: n * fatorial(n - 1)
  # Cálculo da sequência de Fibonacci
  def fibonacci(0), do: 0
  def fibonacci(1), do: 1
  def fibonacci(n), do: fibonacci(n-1) + fibonacci(n-2)
  # Pegar o primeiro elemento de uma lista
  def primeiro(lista), do: hd(lista)
  # Pegar o último elemento de uma lista
  def ultimo(lista), do: Enum.at(lista, -1)

end

# Executando no console
IO.puts "A soma entre 3 e 11 é " <> Integer.to_string(TDSOFT.soma(3, 11))
IO.puts "O fatorial de 0 é " <> Integer.to_string(TDSOFT.fatorial(0))
IO.puts "O fatorial de 5 é " <> Integer.to_string(TDSOFT.fatorial(5))
IO.puts "O 9º número da sequência de fibonacci é " <> Integer.to_string(TDSOFT.fibonacci(9))
IO.puts "O primeiro elemento da lista [2, 4, 3, 2, 55] é " <> Integer.to_string(TDSOFT.primeiro([2, 4, 3, 2, 55]))
IO.puts "O último elemento da lista [2, 4, 3, 2, 55] é " <> Integer.to_string(TDSOFT.ultimo([2, 4, 3, 2, 55]))
