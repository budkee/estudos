# Eficiência algorítmica 

## Análise de Complexidade

Complexidades dos principais algoritmos de ordenação, tanto para o melhor quanto para o pior caso:

| Algoritmo          | Melhor Caso          | Pior Caso             | Caso Médio            |
|--------------------|------------------------|------------------------|------------------------|
| **Bubble Sort**    | \(O(n)\) (quando a lista já está ordenada) | \(O(n^2)\) | \(O(n^2)\) |
| **Insertion Sort** | \(O(n)\) (quando a lista já está ordenada) | \(O(n^2)\) | \(O(n^2)\) |
| **Selection Sort** | \(O(n^2)\) | \(O(n^2)\) | \(O(n^2)\) |
| **Merge Sort**     | \(O(n \log n)\) | \(O(n \log n)\) | \(O(n \log n)\) |
| **Quick Sort**     | \(O(n \log n)\) (quando o pivô é bem escolhido) | \(O(n^2)\) | \(O(n \log n)\) |
| **Heap Sort**      | \(O(n \log n)\) | \(O(n \log n)\) | \(O(n \log n)\) |
| **Counting Sort**  | \(O(n + k)\) (onde \(k\) é o intervalo dos valores) | \(O(n + k)\) | \(O(n + k)\) |
| **Radix Sort**     | \(O(n \cdot k)\) (onde \(k\) é o número de dígitos) | \(O(n \cdot k)\) | \(O(n \cdot k)\) |
| **Bucket Sort**    | \(O(n + k)\) (quando os dados estão uniformemente distribuídos) | \(O(n^2)\) | \(O(n + k)\) |

- **Bubble Sort** e **Insertion Sort** são mais eficientes em listas pequenas ou quase ordenadas.
- **Selection Sort** tem desempenho constante mas não é eficiente para listas grandes.
- **Merge Sort**, **Quick Sort**, e **Heap Sort** são geralmente preferidos para listas grandes devido à sua complexidade \(O(n \log n)\).
- **Counting Sort**, **Radix Sort**, e **Bucket Sort** são eficientes para tipos específicos de dados e distribuições.
