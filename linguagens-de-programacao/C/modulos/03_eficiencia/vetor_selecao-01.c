#include <stdio.h>

int main() {
    
    double A[100];

    // Leitura do vetor A
    for (int i = 0; i < 100; i++) {
        scanf("%lf", &A[i]);
    }

    // Verificação e exibição dos valores menores ou iguais a 10
    for (int i = 0; i < 100; i++) {
        if (A[i] <= 10.0) {
            printf("A[%d] = %.1lf\n", i, A[i]);
        }
    }

    return 0;
}