#include <stdio.h>
#define max 5

// Funções
void troca(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}


void ordenaPontuacao(int n, int v[]) {
    
    int maior;

    for (int i = 0; i < n - 1; i++) {
        maior = i;
        for (int j = n - 1; j > -1; j--) {
            
            if (v[j] > v[maior]){
                maior = j;
            } else {
                troca(&v[i], &v[maior]);
            };        
            //printf("\ni: %d \nj: %d \n", i, j);
            
            //printf("%d \n", v[maior]);
        
        };
    };
}


// Início
int main(void) {

    // Declarações
    int vetor[] = {20, 399, 7, 2, 33};
    int n = sizeof(vetor) / sizeof(vetor[0]);
    
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    };

    printf("\n");

    ordenaPontuacao(n, vetor);

    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    };
    return 0;
}
