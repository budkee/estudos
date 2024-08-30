#include <stdio.h>

// Nó mae[0] ou mae[i]
int mae(int i)
{
    return (i-1)/2;
};

// Filhe esquerdo e[i]
int esquerdo(int i)
{
    return 2 * (i+1) - 1;
};
// Filhe direito d[i]
int direito(int i)
{
    return 2 * (i+1);
};

/*  ---------------- Problema ---------------- 
*
*   Seja um vetor de números inteiros S com n > 0 elementos e um índice i. 
*   Se S é visto como uma árvore binária, estabeleça a propriedade max-heap (2) para a sub-árvore de S com raiz S[i], supondo que as sub-árvores esquerda e direita do nó i de S são max-heaps.
* 
*/

// Manutenção da Propriedade Max-Heap 
void desce(int n, int S[MAX], int i)
{
    /*
        Tempo de execução de pior caso: O(log_2 n) ou O(lg n) => é proporcional à altura da árvore binária correspondente ao vetor
    */
    int e, d, maior;

    e = esquerdo[i];
    d = direito[i];

    if (e < n && S[e] > S[i])
        maior = e;
    else
        maior = i;

    if (d < n && S[d] > S[maior])
        maior = d;
    if (maior != i)
    {
        troca(&S[i], &S[maior]);
        desce(n, S, maior);
    }
}

// Construção da Propriedade Max-Heap 
void constroi_max_heap(int n, int S[MAX])
{
    /*
        Dado um vetor desordenado, e seu tamanho n, o tempo de execução pode ser visto pela:

            - Primeira análise: O(n lg n)
            - Análise mais apurada: O(n)
    */
    int i;

    for (i = n/2 - 1; i >= 0; i--)
    { 
        desce(n, S, i);
    }
}

// Alteração da Prioridade em um Max-Heap 
void sobe(int n, int S[MAX], int i)
{
    /*
        Tempo de execução no pior caso: O(lg n) => é proporcional à altura da árvore binária correspondente ao vetor
    */
    while (S[mae(i)] < S[i])
    {
        troca(&S[i], &S[mae(i)]);
        i = mae(i);
    }
}

/* ---------------- Lista de Prioridades ----------------

    Aplicações: Simulador de eventos, Escalonamento de tarefas em um computador...

    * Exemplo de um simulador de eventos | Modelagem de aterrissagem e decolagem de um aeroporto

        Imagine um simulador de um aeroporto que modela a decolagem e aterrissagem de aviões. Os eventos podem incluir:

	    •	Aterrissagem de um avião
	    •	Decolagem de um avião
	    •	Manutenção de uma pista
	    •	Troca de turno dos controladores de tráfego aéreo

        Cada um desses eventos teria um timestamp indicando o momento exato em que deve ocorrer. A lista de prioridades garantiria que os eventos são processados na ordem correta:

	    •	Inserção de Eventos: Se um avião está agendado para decolar às 10:00, e outro para aterrissar às 09:50, o evento de aterrissagem será inserido na frente do evento de decolagem na fila de eventos.
	    •	Processamento de Eventos: O simulador remove e processa o evento de aterrissagem primeiro, seguido pelo evento de decolagem.
    
    // ---------------- Lista de Max-Prioridades e Min-Prioridades ----------------
        
        Um max-heap pode ser usado para implementar uma lista de max-prioridades ou min-prioridades.

        * Propriedade Max-Heap => S[mae(i)] >= S[i]: Ordem decrescente
        * Propriedade Min-Heap => S[mae(i)] <= S[i]: Ordem crescente

        => Operações

            1. Inserção de um elemento em S: 
                
                desce() => O(lg n)
            
            2. Consulta da maior prioridade em S: 
            
                consulta_max() => O(1)
            
            3. Remoção do elemento de maior prioridade em S: 
            
                extrai_max() => O(lg n)
            
            4. Aumento da prioridade de um elemento em S: 
            
                sobe() => O(lg n)
*/ 
// 1. Inserção de um elemento em S
void insere_lista(int *n, int S[MAX], int p)
{
    /*
        Tempo de execução: O(lg n)
    */
    S[*n] = p;
    *n = *n + 1;
    sobe(*n, S, *n - 1);
}
// 2. Consulta da maior prioridade em S
int consulta_maxima(int S[MAX])
{
    /*
        Retorna o valor de maior prioridade na lista;
        Tempo de Execução: O(1) | Constante
    */
    return S[0];  
}

// 3. Remoção do elemento de maior prioridade em S
int extrai_max(int *n, int S[MAX])
{
    int maior;

    if (*n > 0) 
    { 
        maior = S[0];
        S[0] = S[*n - 1];
        *n = *n - 1;
        desce(*n, S, 0); // Tempo de execução: O(lg n) | logarítmica
        return maior;
    }
    else {
        return ?
    }
}

// 4. Aumento da prioridade de um elemento em S
void aumenta_prioridade(int n, int S[MAX], int i, int p)
{
    if (p < S[i]){
        printf("Erro: nova prioridade é menor que da célula\n");
    } else {
        S[i]= p;
        sobe(n, S, i); // Tempo de execução: O(lg n) | logarítmica
    }
}

/* ---------------- Ordenação com heaps ----------------



*/

void heapsort(int n, int S[MAX])
{

    // Tempo de execução: O(lg n) | logarítmica

    int i;

    constroi_max_heap(n, S); // O(n) | Constante
    for (i = n - 1; i > 0; i--)
    {
        troca(&S[0], &S[i]); 
        n--;
        desce(n, S, 0); // O(lg n) | Logarítmico
    }
}