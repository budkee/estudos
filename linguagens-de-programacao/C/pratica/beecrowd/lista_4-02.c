// Bibliotecas e definições
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Função de comparação para a função qsort
int comparar(const void *a, const void *b) {
    return strcmp((const char *)a, (const char *)b);
}

int main(void) {
    int N;

    while (scanf("%d", &N) != EOF) {
        
        char codigos[N][5];  // Matriz para armazenar os códigos

        for (int i = 0; i < N; i++) {
            scanf("%s", codigos[i]);
        }

        // Ordena os códigos usando a função qsort
        qsort(codigos, N, sizeof(codigos[0]), comparar);

        for (int i = 0; i < N; i++) {
            printf("%s\n", codigos[i]);
        }
    }

    return 0;
}
