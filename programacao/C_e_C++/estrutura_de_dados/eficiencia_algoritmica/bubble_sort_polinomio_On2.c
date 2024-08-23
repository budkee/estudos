#include <stdio.h>
#include <math.h>

// Função para inverter o array de coeficientes
void inverter_array(double a[], int n) {
    for (int i = 0; i < n / 2; i++) {
        double temp = a[i];
        a[i] = a[n - 1 - i];
        a[n - 1 - i] = temp;
    }
}

// Função para calcular o valor do polinômio em um ponto x com coeficientes a[]
double calcular_polinomio(int n, double a[], double x) {
    double resultado = 0.0;

    // Calcula o valor do polinômio utilizando uma abordagem direta e eficiente
    for (int i = 0; i < n; i++) {
        // Adiciona o termo a_i * x^i ao resultado
        resultado += a[i] * pow(x, i);
    }

    return resultado;
}

int main(void) {
    int n;
    printf("Digite o número de coeficientes: ");
    scanf("%d", &n);

    double a[n];
    printf("Digite os coeficientes:\n");
    for (int i = 0; i < n; i++) {
        scanf("%lf", &a[i]);
    }

    // Inverter o array de coeficientes
    inverter_array(a, n);

    double x;
    printf("Digite o valor de x: ");
    scanf("%lf", &x);

    double resultado = calcular_polinomio(n, a, x);
    printf("O valor do polinômio em x = %.2lf é %.2lf\n", x, resultado);

    return 0;
}
