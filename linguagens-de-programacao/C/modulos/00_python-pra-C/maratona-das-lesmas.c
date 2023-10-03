#include <stdio.h>

/*
    Sobre o programa
    
    Esta tarefa é baseada em uma tarefa similar da Olimpíada Cearence de Informática de 2014. 
    Na corrida de lesmas, cada lesma é classificada em um nível dependendo de sua velocidade. 
    O problema é que as lesmas mais rápidas também se cansam mais rapidamente. 
    
    Assim:
    - se sua velocidade é menor ou igual a 10 cm/h, então ela consegue andar por 3 h até parar;
    - se sua velocidade é maior que 10 cm/h e menor ou igual a 20 cm/h, então ela consegue andar por 2 h até parar;
    - se sua velocidade é maior que 20 cm/h e menor ou igual a 100 cm/h, então ela consegue andar por 1 h até parar.

    Suponha que não existem lesmas que rastejam mais rapidamente que 100 cm/h.

    Sua tarefa é identificar qual é a velocidade da lesma mais rápida que pode competir em uma maratona de uma certa duração.

*/

/*
    Entrada

    a. deverá ser composta de um número n inteiro na primeira linha
    b. seguida de n linhas, cada uma representando a velocidade de uma lesma como um número inteiro
    c. um número inteiro d, representando a duração em horas da competição 

    Saída

    - uma única linha representando a velocidade da lesma mais rápida que pode competir.

*/

int main() {

    // Declaração das variáveis
    int i, n, tempo, limite;
    int maxima = 0;
    int velocidades[100];
    
    // Leitura das variáveis
    
    // Entrada a
    scanf("%d", &n);    

    // Duração da competição (Entrada c)
    scanf("%d", &tempo);

    // Guardando as velocidades (Entrada b)
    for (i = 0; i < n; i++ ) {

        scanf("%d", &velocidades[i]);
        
    };

    // Descobrindo a velocidade limite das lesmas
    if (tempo == 1) {

        limite = 100;
    
    } else if (tempo == 2) {
    
        limite = 20;
    
    } else {
    
        limite = 10;
    
    };

    // Calculando a maior velocidade de lesmas qualificadas
    for (i = 0; i < n; i++) {

        if (velocidades[i] > maxima && velocidades[i] <= limite) {

            maxima = velocidades[i];

        };
    };

    // Imprima a saída
    printf("%d", maxima);

};