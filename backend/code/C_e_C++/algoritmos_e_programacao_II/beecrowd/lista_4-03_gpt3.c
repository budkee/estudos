#include <stdio.h>
#include <stdlib.h>

// Função de comparação para qsort
int compare(const void *a, const void *b) {
    int intA = *((int *)a);
    int intB = *((int *)b);

    if (intA % 2 == 0 && intB % 2 == 0) {
        return intA - intB; // Ordenar pares em ordem crescente
    }
    if (intA % 2 != 0 && intB % 2 != 0) {
        return intB - intA; // Ordenar ímpares em ordem decrescente
    }
    if (intA % 2 == 0) {
        return -1; // intA é par, coloque antes de intB
    }
    return 1; // intB é par, coloque antes de intA
}

int main() {
    int N;
    scanf("%d", &N);

    int values[N];

    for (int i = 0; i < N; i++) {
        scanf("%d", &values[i]);
    }

    qsort(values, N, sizeof(int), compare);

    for (int i = 0; i < N; i++) {
        printf("%d\n", values[i]);
    }

    return 0;
}