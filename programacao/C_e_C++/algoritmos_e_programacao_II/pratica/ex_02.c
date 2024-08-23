#include <stdio.h>
#include <stdlib.h>

#define MAX 100

// Encontra os dois maiores valores num vetor
void dois_maiores(int n, int v[MAX], int *pr, int *seg) {

    
    for (int i=0; i < n; i++) {

        if (v[i] > *pr) {
            *seg = *pr;
            *pr = v[i];
        } else if (v[i] > *seg) {
            *seg = v[i];
        }
    }

    
}

int main(void) {

    int n;
    printf("Quantos elementos tem o vetor? ");
    scanf("%d", &n); 
    
    int v[MAX];

    // Criação do vetor
    for (int i = 0; i < n; i++) {
        v[i] = rand() % 100;
    }
    
    printf("\n");
    // vetor aleatório
    printf("O vetor criado é: ");

    for (int i = 0; i < n; i++) {
        printf("%d ", v[i]);
    };
    
    int pr, seg;
    dois_maiores(n, v, &pr, &seg);
    
    printf("\n");
    printf("O maior elemento é %d e o segundo maior é %d\n", pr, seg);

    return 0;
}