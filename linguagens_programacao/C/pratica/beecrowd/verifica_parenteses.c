#include <stdio.h>
#include <string.h>

#define MAX_SIZE 1000

int verificaParenteses(char expressao[MAX_SIZE]) {
    int contador = 0;

    for (int i = 0; expressao[i] != '\0'; i++) {
        if (expressao[i] == '(') {
            contador++;
        } else if (expressao[i] == ')') {
            contador--;
            if (contador < 0) {
                return 0; // Mais ')' do que '('
            }
        }
    }

    return contador == 0 ? 1 : 0; // Verifica se o número de '(' é igual ao número de ')'
}

int main(void) {
    char expressao[MAX_SIZE];

    // Abre o arquivo de entrada em modo de leitura
    while (scanf("%[^\n]%*c", expressao) != EOF) {
        if (verificaParenteses(expressao)) {
            printf("correct\n");
        } else {
            printf("incorrect\n");
        }
    }

    return 0;
}
