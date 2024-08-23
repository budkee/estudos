#include <stdio.h>
#include <stdbool.h>

/* Sobre o Bubble Sort 
*
*   Realiza trocas sucessivas do início ao fim contendo duas iteráveis (i, j), com os seguintes limites:
*   
*   tamanho da lista = n
*   
*   > Início
*   n = i + 1
*   n = i + j + 1
*
*   > Fim
*   i = n - 1
*   j = n - i - 1
*
*/

void bubble_sort(int lista[], int n){

    // Percorre cada elemento da lista
    for (int i = 0; i < n - 1; i++) {
        // Trocou?
        bool trocou = false;

        // Compara em par os elementos
        for (int j = 0; j < n - i - 1; j++) {
            // Se o primeiro for maior que o segundo, troca
            if (lista[j] > lista[j+1]){
                int temp = lista[j];
                lista[j] = lista[j + 1];
                lista[j + 1] = temp;
                trocou = true;
            }
        }

        // Caso nenhuma troca seja feita, finalize a função
        if (!trocou){
            break;
        }
    }



}

int main(void) {

    // Definição do array
    int arr[] = {92, 22, 3, 1, 23, 31, 0};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Imprime o endereço de memória
    // printf("%d", arr);
    printf("Array antes: ");
    for (int a = 0; a < n; a++){
        printf("%d ", arr[a]);
    }

    // Ordenação
    bubble_sort(arr, n);

    printf("\nArray ordenado: ");
    for (int a = 0; a < n; a++){
        printf("%d ", arr[a]);
    }

    return 0;
}
