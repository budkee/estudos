#include <stdio.h>

int main() {
    int N[1000];
    int T;

    // Leitura do valor T
    scanf("%d", &T);

    // Preenchimento do restante do vetor com 
    int valor = 0;
    for (int i = 0; i < 1000; i++) {
        
        N[i] = valor;
        valor++;

        if (valor == T) {
            valor = 0;
        }
    }

    // Exibição do vetor
    for (int i = 0; i < 1000; i++) {
        printf("N[%d] = %d\n", i, N[i]);
    }

    return 0;
}
