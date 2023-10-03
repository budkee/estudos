#include <stdio.h>

int main() {
    int N[10];
    int V;

    // Leitura do valor V
    scanf("%d", &V);

    // Atribuição do valor de V à primeira posição do vetor
    N[0] = V;

    // Preenchimento do restante do vetor com o dobro do valor anterior
    for (int i = 1; i < 10; i++) {
        N[i] = N[i - 1] * 2;
    }

    // Exibição do vetor
    for (int i = 0; i < 10; i++) {
        printf("N[%d] = %d\n", i, N[i]);
    }

    return 0;
}
