void troca(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int referencial(int v[], int menor, int maior) {
    // 
    int pivot = v[maior];
    int i = (menor - 1);

    // Percorre uma parte do vetor e verifica se é menor ou igual ao pivot
    for (int j = menor; j < maior; j++)
    {
        if (v[j] <= pivot)
        {
            i++;
            troca(&v[i], &v[j]);
        }
    }

    troca(&v[i + 1], &v[maior]);

    return (i + 1);
}

void quicksort(int v[], int menor, int maior){
    
    if (menor < maior) {

        // Encontra o indice referencial
        int i = referencial(v, menor, maior);

        // Ordena os elementos antes e depois que o referencial
        quicksort(v, menor, i - 1);
        quicksort(v, i + 1, maior);
    }
}