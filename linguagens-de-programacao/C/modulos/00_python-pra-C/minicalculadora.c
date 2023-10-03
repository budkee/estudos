#include <stdio.h>

int main() {
    // Declaração de variáveis
    int i, n;
    float n1, n2;
    float resultado;
    char operador; // Caractere ASCII

    // Leitura do número de operações
    scanf("%d", &n);

    for (i = 0; i < n; i++) {

        // Leitura (dinâmica) das variáveis
        scanf("%f %c %f", &n1, &operador, &n2);

        // Verifique se o operador é... 
        if (operador == '/') {
            // de divisão
            resultado = n1 / n2;
            printf("%.1f\n", resultado);

        } else if (operador == '*') {
            // de multiplicação
            resultado = n1 * n2;
            printf("%.1f\n", resultado);

        } else if (operador == '+') {
            // de adição
            resultado = n1 + n2;
            printf("%.1f\n", resultado);

        } else if (operador == '-') {
            // de subtração
            resultado = n1 - n2;
            printf("%.1f\n", resultado);

        } else {
            
            printf("Erro: operador não reconhecido\n");
        
        };
    };
    
    return 0;
}