#include <stdio.h>
#include <string.h>

// Estrutura para armazenar as strings originais e seus tamanhos
struct StringInfo {
    char str[51];
    int length;
};

// Função de comparação para qsort
int compare(const void *a, const void *b) {
    struct StringInfo *strA = (struct StringInfo *)a;
    struct StringInfo *strB = (struct StringInfo *)b;

    if (strA->length == strB->length) {
        return strcmp(strA->str, strB->str);
    }

    return strA->length - strB->length;
}

int main(void) {
    int N;
    scanf("%d", &N);

    while (N--) {
        int M;
        scanf("%d", &M);
        getchar(); // Ler o caractere de nova linha após M

        struct StringInfo strings[50];

        // Ler as strings e calcular seus tamanhos
        for (int i = 0; i < M; i++) {
            fgets(strings[i].str, 51, stdin);
            strings[i].length = strlen(strings[i].str) - 1; // Exclui o caractere de nova linha
        }

        // Ordenar as strings
        qsort(strings, M, sizeof(struct StringInfo), compare);

        // Imprimir as strings ordenadas
        for (int i = 0; i < M; i++) {
            printf("%s", strings[i].str);
        }

        if (N > 0) {
            printf("\n"); // Imprimir linha em branco entre casos de teste
        }
    }

    return 0;
}
