defmodule OrdenaFuncional do

  def quicksort([]), do: []
  def quicksort([pivot | resto]), do: quicksort(for x <- resto, x <= pivot, do: x) ++ [pivot] ++ quicksort(for x <- resto, x > pivot, do: x)

end

# Teste no console
tempo_inicio = :erlang.monotonic_time(:millisecond)
IO.inspect(OrdenaFuncional.quicksort([7, 2, 1, 6, 8, 5, 3, 4]))
tempo_fim = :erlang.monotonic_time(:millisecond)
tempo_execucao = tempo_fim - tempo_inicio
IO.puts("Tempo de execução: #{tempo_execucao} ms")
