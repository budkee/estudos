package sorting;

public class QuickSort {

    public static void main(String[] args) {
        int[] array = {7, 2, 1, 6, 8, 5, 3, 4};
        
        System.out.println("Array original:");
        printArray(array);
        
        quickSort(array, 0, array.length - 1);
        
        System.out.println("\nArray ordenado:");
        printArray(array);
    }
    
    public static void quickSort(int[] array, int inicio, int fim) {
        if (inicio < fim) {
            int indicePivot = particionar(array, inicio, fim);
            quickSort(array, inicio, indicePivot - 1);
            quickSort(array, indicePivot + 1, fim);
        }
    }
    
    public static int particionar(int[] array, int inicio, int fim) {
        int pivot = array[fim];
        int indicePivot = inicio;
        
        for (int i = inicio; i < fim; i++) {
            if (array[i] <= pivot) {
                trocar(array, i, indicePivot);
                indicePivot++;
            }
        }
        
        trocar(array, indicePivot, fim);
        
        return indicePivot;
    }
    
    public static void trocar(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    
    public static void printArray(int[] array) {
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
