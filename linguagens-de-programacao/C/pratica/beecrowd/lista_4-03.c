// Bibliotecas e definições
#include <stdio.h>
#include <stdlib.h>

// Funções
void troca(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int compara_cresc(const void *a, const void *b){
    return 
}
// Programa
int main(void) {

    // Número de entradas
    int n;
    scanf("%d", &n);

    // Alocação dinâmica
    int *numeros = (int *)malloc(n * sizeof(int));

    // Leitura dos valores
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &numeros[i]);
    }

    // Números antes
    for (int i = 0; i < n; i++)
    {
        printf("%d ", numeros[i]);
    }

    // Ordenação pelos critérios
    for (int i = 0; i < n; i++){ 
        
        // Se for par: ordem crescente
        if (numeros[i] % 2 == 0) {

            quicksort(numeros, 0, n - 1);
        
        } 
    }

    // Números depois
    for (int i = 0; i < n; i++)
    {
        printf("%d ", numeros[i]);
    }

    // Libere a memória alocada dinamicamente
    free(numeros);

    return 0;
}
