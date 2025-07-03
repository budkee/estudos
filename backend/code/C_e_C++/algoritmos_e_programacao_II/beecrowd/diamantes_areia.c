#include <stdio.h>

#define MAX 1001

int contarDiamantes(char str[]) {
    int count = 0;
    int diamantes = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == '<') {
            count++;
        } else if (str[i] == '>' && count > 0) {
            count--;
            diamantes++;
        }
    }

    return diamantes;
}

int main(void) {
    int N, result;
    
    scanf("%d", &N);  // Leitura do número de casos de teste

    for (int t = 0; t < N; t++) {
        char str[MAX];
        scanf("%s", str);  // Agora lê uma string, que pode conter espaços
        result = contarDiamantes(str);
        printf("%d\n", result);
    }

    return 0;
}
