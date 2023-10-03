#include <stdio.h>
#define MAX 10

void troca(int *a, int *b) {
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;

}


void selectionsort(int n, int v[])
{
  int i, j, min;
 
  for (i = 0; i < n - 1; i++) {
    min = i;
 
    for (j = i+1; j < n; j++)
      if (v[j] < v[min])

	      min = j;
    troca(&v[i], &v[min]);

  }

}

// Início
int main(void) {

    // Declarações
    int vetor[] = {2, 3, 4, 1, 0};
    int n = sizeof(vetor) / sizeof(vetor[0]);

    selectionsort(n, vetor);
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    };
    return 0;
}
