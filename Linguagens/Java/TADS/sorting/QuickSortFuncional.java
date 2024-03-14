package sorting;

import java.util.Arrays;

public class QuickSortFuncional {

    // ----------------- Main --------------------
    public static void main(String[] args) {
        int[] array = {7, 2, 1, 6, 8, 5, 3, 4};

        System.out.println("Array original:");
        printArray(array);

        // Captura o tempo de início
        long startTime = System.currentTimeMillis(); 

        // Realiza a ordenação
        int[] sortedArray = quickSort(array);
        
        // Captura o tempo de fim
        long endTime = System.currentTimeMillis(); 

        System.out.println("\nArray ordenado:");
        printArray(sortedArray);

        // Calcula a duração da execução em milissegundos
        long duration = endTime - startTime; 
        System.out.println("\nTempo de execução: " + duration + "ms");
        
    }

    // ----------------- Ordenação --------------------
    public static int[] quickSort(int[] array) {
        if (array.length <= 1) {
            return array;
        }

        int pivot = array[array.length - 1];
        
        int[] menores = Arrays.stream(array)
                              .limit(array.length - 1)
                              .filter(x -> x <= pivot)
                              .toArray();
        
        int[] maiores = Arrays.stream(array)
                              .limit(array.length - 1)
                              .filter(x -> x > pivot)
                              .toArray();
        
        return concat(quickSort(menores), new int[]{pivot}, quickSort(maiores));
    }

    // ----------------- Concatenação --------------------
    public static int[] concat(int[] a, int[] b, int[] c) {
        int[] result = new int[a.length + b.length + c.length];
        System.arraycopy(a, 0, result, 0, a.length);
        System.arraycopy(b, 0, result, a.length, b.length);
        System.arraycopy(c, 0, result, a.length + b.length, c.length);
        return result;
    }

    // ----------------- Saída --------------------
    public static void printArray(int[] array) {
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
