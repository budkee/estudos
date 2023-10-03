#include <stdio.h>

int main() {
    double N[100];
    double X;

    // Leitura do valor T
    scanf("%lf", &X);

    // Preenchimento do vetor 
    N[0] = X;
    for (int i = 0; i < 100; i++) {
        
        N[i + 1] = N[i]/2.0;
    }

    // Exibição do vetor
    for (int i = 0; i < 1000; i++) {
        printf("N[%d] = %.4lf\n", i, N[i]);
    }

    return 0;
}
