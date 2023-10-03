#include <stdio.h>
#define MAX 10

void troca(int *a, int *b) {
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;

}


void insertionSort(int n, int v[])

{
  // Declarações
  int i, j, temp;
  
  /* Loop estático */
  // Intervalo: [1, n[
  for (i = 1; i < n; i++) {
    
    // Atribua a temp o valor que o vetor está apontando
    temp = v[i];
  
    /* Loop dinâmico */
    // Intervalo: [i-1, 0] e v[j] > temp
    for (j = i - 1; j >= 0 && v[j] > temp; j--)
      
      // Troca o elemento
      v[j+1] = v[j];
    
    // Atribua ao próximo elemento o valor de x;
    v[j+1] = temp;
  }

}

/*
  Nesta função ocorre que o vetor estático [i] percorre da esquerda para direita, enquanto que o vetor dinâmico [j] percorre no sentido oposto, a partir do elemento a esquerda de [i], ou seja, [i-1].
*/