#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 1000

void troca(int *a, int *b);
void copia_tmp(int n, int v[], int tmp[]);
void bubblesort(int n, int v[]);
void selectionsort(int n, int v[]);
void insertionsort(int n, int v[]);


int main(void)
{
  int i, v[MAX], tmp[MAX];
  int n = MAX;
  clock_t inicio, fim;

  /* initialize random seed: */
  srand (time(NULL));

  for (i = 0; i < n; i++)
    v[i] = rand();  // vetor aleatório
    //v[i] = i;     // vetor ordenado
    //v[i] = n - i; // vetor decrescente
    

  printf("%d elementos\n", n);

  
  copia_tmp(n, v,tmp);
  inicio = clock();
  bubblesort(n, tmp);
  fim = clock();
  printf("BUBBLE: %g segundos\n", (fim - inicio) / (float) CLOCKS_PER_SEC);

  copia_tmp(n, v,tmp);
  inicio = clock();
  selectionsort(n, tmp);
  fim = clock();
  printf("SELECTION: %g segundos\n", (fim - inicio) / (float) CLOCKS_PER_SEC);
  
  copia_tmp(n, v,tmp);
  inicio = clock();
  insertionsort(n, tmp);
  fim = clock();
  printf("INSERTION: %g segundos\n", (fim - inicio) / (float) CLOCKS_PER_SEC);

  return 0;
}

void troca(int *a, int *b)
{
  int aux;
  aux = *a;
  *a = *b;
  *b = aux;
}

void copia_tmp(int n, int v[], int tmp[])
{
  for (int i = 0; i < n; i++)
    tmp[i] = v[i];
}

void bubblesort(int n, int v[])
{
  int i, j;
  for (i = n - 1; i > 0; i--)
    for (j = 0; j < i; j++)
      if (v[j] > v[j+1])
	troca(&v[j], &v[j+1]);
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

void insertionsort(int n, int v[])
{
  int i, j, x;
  for (i = 1; i < n; i++) {
    x = v[i];
    for (j = i - 1; j >= 0 && v[j] > x; j--)
      v[j+1] = v[j];
    v[j+1] = x;
  }
}


