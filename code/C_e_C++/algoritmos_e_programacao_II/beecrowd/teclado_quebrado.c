#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100001

void processInput(char *input) {
    char output[MAX_SIZE];
    int outputIndex = 0;
    int homeIndex = -1; // Inicializado com -1 para indicar nenhum '[' encontrado

    for (int i = 0; input[i] != '\0'; i++) {
        if (input[i] == '[') {
            homeIndex = outputIndex;
        } else if (input[i] == ']') {
            outputIndex = homeIndex;
        } else {
            output[outputIndex++] = input[i];
        }
    }

    output[outputIndex] = '\0';  // Null-terminate the string

    if (outputIndex > 0) {
        
        // Verifica se há texto Beiju para imprimir
        if (homeIndex > 0) {
            printf("Beiju");
        }
        puts(output);
    }
}

int main(void) {
    char input[MAX_SIZE];

    // Ler enquanto houver entrada do arquivo
    while (scanf("%s", input) != EOF) {
        processInput(input);
    }

    return 0;
}
