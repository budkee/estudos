#include <stdio.h>

int main() {
    int X[10];

    // Leitura dos valores do vetor
    for (int i = 0; i < 10; i++) {
        scanf("%d", &X[i]);
    }

    // Substituição dos valores nulos e negativos por 1
    for (int i = 0; i < 10; i++) {
        if (X[i] <= 0) {
            X[i] = 1;
        }
    }

    // Exibição do vetor modificado
    for (int i = 0; i < 10; i++) {
        printf("X[%d] = %d\n", i, X[i]);
    }

    return 0;
}
