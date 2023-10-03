#include <stdio.h>
#define MAX 10
/* Funções */
void troca(int *a, int *b) {
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;

}

void selectionsort(int n, int v[])
{
    // Declaração
    int i, j, min;
 
    // Intervalo: [0, n-1[
    for (i = 0; i < n - 1; i++) {
        
        // Atribua i como o mínimo do vetor
        min = i;

        // Intervalo: [i+i, n[
        for (j = i+1; j < n; j++)
            
            // Condição 
            if (v[j] < v[min])

    // Atribua o j como mínimo do vetor
	min = j;

    // Troca os elementos
    troca(&v[i], &v[min]);

  }

}

/* Início */
int main(void){

    int vetor[] = {8, 4, 3, 0, 1, 7};
    int n = sizeof(vetor) / sizeof(vetor[0]);
    
    // Vetor desordenado
    for (int k = 0; k < n; k++){

        printf("%d ", vetor[k]);

    };
    printf("\n");

    selectionsort(n, vetor);
    
    // Vetor ordenado
    for (int i = 0; i < n; i++) {  
        
        printf("%d ", vetor[i]);
    
    };

    return 0;

} 
/* Fim */