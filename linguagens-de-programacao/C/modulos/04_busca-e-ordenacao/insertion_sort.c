#include <stdio.h>
#define MAX 10

void troca(int *a, int *b) {
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;

}


void insertionSort(int n, int j, int x, int v[])

{
  int i, j, x;
  
  for (i = 1; i < n; i++) {
    x = v[i];
    
    for (j = i - 1; j >= 0 && v[j] > x; j--)
      v[j+1] = v[j];
    
    v[j+1] = x;
  }

}