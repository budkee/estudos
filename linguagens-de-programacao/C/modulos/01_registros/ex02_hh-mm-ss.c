#include <stdio.h>

/* Este programa recebe dois horários no formato hh:mm:ss e retorna o horário decorrido entre eles.  */

typedef struct {

    int hh;
    int mm;
    int ss;
    
    } horario;

int main(void) {

    // Declaração de variáveis
    // - Cria e lê os vetores
    horario horarioDecorrido;
    horario horario0;
    horario horario1;
    horario bandeja;

    // Entrada dos vetores
    // - Vetor horario0
    printf("Informe o horário inicial (hh:mm:ss): ");
    
    scanf("%d:%d:%d", &horario0.hh, &horario0.mm, &horario0.ss);

    // Verificação
    printf("Horário Inicial: %d:%d:%d\n", horario0.hh, horario0.mm, horario0.ss);

    // - Vetor horario1
    printf("Informe o horário final (hh:mm:ss): ");

    scanf("%d:%d:%d", &horario1.hh, &horario1.mm, &horario1.ss);

    // Verificação
    printf("Horário Final: %d:%d:%d\n", horario1.hh, horario1.mm, horario1.ss);
    

    // Manipulação: calcule a diferença entre os dois horários.

    // Total de segundos

    // Casos de segundos
    if (horario1.ss < horario0.ss) {

        horarioDecorrido.ss = (60 + horario1.ss) - horario0.ss;

    } else if (horario1.ss == horario0.ss) {

        horarioDecorrido.ss = 0;

    } else {

        horarioDecorrido.ss = horario1.ss - horario0.ss;
    
    }

    // Total de minutos

    // Casos de minutos
    if (horario1.mm < horario0.mm) {

        horarioDecorrido.mm = (60 + horario1.mm) - horario0.mm;

        bandeja.mm = horario1.mm;

    } else if (horario1.mm == horario0.mm) {

        horarioDecorrido.mm = 0;

    } else {

        horarioDecorrido.mm = horario1.mm - horario0.mm;
    
    }

    // Total de horas

    // Casos de horas
    // Caso menos provável
    if (horario1.hh < horario0.hh) {

        horarioDecorrido.hh = (60 + horario1.hh) - horario0.hh;

    // Caso exato
    } else if (horario1.hh == horario0.hh) {

        horarioDecorrido.hh = 0;
    
    // Caso mais provável (horario1.hh > horario0.hh)
    } else {

        horarioDecorrido.hh = horario1.hh - horario0.hh - 1;
    
    }

    // Imprima o resultado final
    
    printf("O horário decorrido foi de %d:%d:%d\n", horarioDecorrido.hh, horarioDecorrido.mm, horarioDecorrido.ss);

    return 0;
}

