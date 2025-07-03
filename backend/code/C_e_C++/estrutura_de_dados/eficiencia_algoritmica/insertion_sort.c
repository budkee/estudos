#include <stdio.h>

/* Sobre o Insertion Sort: trabalha com posições de iteráveis
*
*   Percorre a lista do início ao fim, assumindo que o primeiro elemento já esteja ordenado. Contendo duas iteráveis (i, j), com os seguintes limites:
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

void insertion_sort(int lista[], int n){

    // Percorre a lista a partir da segunda posição
    for (int i = 1; i < n; i++){
        // Define a chave
        int chave = lista[i];
        // Inicializa a segunda iterável na primeira posição
        int j = i - 1;

        // Verifica se está dentro da lista e se [j] é maior que a chave (se o elemento da esquerda é maior que o da direita)
        while (j >= 0 && lista[j] > chave)
        {
            // Move o elemento que está em [j] para direita
            lista[j + 1] = lista[j];
            // Atualiza o [j] 
            j = j - 1;
        }

        // Insere a chave
        lista[j + 1] = chave;
    }
}

void print_lista(int lista[], int n){
    for (int a = 0; a < n; a++){
        printf("%d ", lista[a]);
    }
    printf("\n");
}

int main(void){

    // Definição do array
    int arr[] = {2, 5, 0, 33, 312, 22, 9};
    int n = sizeof(arr) / sizeof(n);

    printf("Array antes: \n");
    print_lista(arr, n);

    insertion_sort(arr, n);

    printf("Array depois: \n");
    print_lista(arr, n);

    return 0;
}
