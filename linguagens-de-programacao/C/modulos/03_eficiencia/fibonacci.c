#include <stdio.h>

// Declaração da função

// Unsigned: utilizado para permitir a entrada de apenas números inteiros não negativos
unsigned long fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else {
        
        // Declaração do vetor e inicializacao do primeiro e segundo elemento
        unsigned long fib[n+1];
        fib[0] = 0;
        fib[1] = 1;
        
        // Calculo do número de fibonacci a partir do 3ro elemento (indice 2)
        for (int i = 2; i <= n; i++) {
            fib[i] = fib[i-1] + fib[i-2];
        }
        
        // Retorno do valor
        return fib[n];
    }
}

// Início do modulo principal
int main() {
    
    // Declaracao do numero de testes
    int T;
    
    // Leitura do valor
    scanf("%d", &T);
    
    // Leitura do valor dos casos de teste
    for (int i = 0; i < T; i++) {
        
        // Declaracao do caso da vez
        int N;
        
        // Leitura
        scanf("%d", &N);

        // Cálculo do valor na sequencia
        unsigned long result = fibonacci(N);

        // Saida
        printf("Fib(%d) = %llu\n", N, result);
    }

    return 0;
}
