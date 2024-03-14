#include <stdio.h>

// Função para calcular o Fibonacci e contar as chamadas recursivas
int fibonacci(int n, int *calls) {
    (*calls)++; // Incrementa o contador de chamadas

    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacci(n - 1, calls) + fibonacci(n - 2, calls);
    }
}

int main(void) {
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        int X;
        scanf("%d", &X);

        int calls = 0; // Inicializa o contador de chamadas
        int result = fibonacci(X, &calls);

        printf("fib(%d) = %d calls = %d\n", X, calls - 1, result);
    }

    return 0;
}
