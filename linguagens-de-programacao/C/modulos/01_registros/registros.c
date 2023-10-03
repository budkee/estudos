#include <stdio.h>

/*
  Lê nomes, notas e presenças de cada aluno, e então
  a quantidade de aulas. Adiciona um bônus de 10%
  para quem assistiu pelo menos metade das aulas,
  e escreve o relatório final.
  
  Exemplo de entrada:
3
Fulano
8.5 7
Ciclano
6.0 2
Beltrano
7.0 4
9

  Exemplo de entrada com comentários meus (não dá pra usar no programa):
3        ->  n
Fulano   -> nome aluno 1
8.5 7    -> nota e nº de presenças do aluno 1
Ciclano  -> aluno 2
6.0 2
Beltrano -> aluno 3
7.0 4
9        -> número de aulas do semestre


Exemplo de saída:
Fulano (7): 9.4
Ciclano (2): 6.0
Beltrano (4): 7.0

*/

#define MAX_NOME 20

typedef struct {
  char nome[MAX_NOME+1];
  float nota;
  int presencas;
} aluno;


int main(void) {
  // Lê a quantidade de alunos
  int n;
  scanf("%d", &n);

  // Cria e lê vetor
  aluno meus_alunos[n];
  //tipo nome_do_vetor[tamanho];
  //int valores[n];
  
  for (int i = 0; i < n; i++)
    //era assim: scanf("%s%f%d", nomes[i], &notas[i], &presencas[i]);  
    scanf("%s%f%d", meus_alunos[i].nome, &meus_alunos[i].nota, &meus_alunos[i].presencas);

  // Lê quantidade de aulas
  int aulas;
  scanf("%d", &aulas);

  // Adiciona bônus
  for (int i = 0; i < n; i++)
    if (meus_alunos[i].presencas >= aulas / 2.0)
      meus_alunos[i].nota *= 1.1;

  // Escreve relatório
  for (int i = 0; i < n; i++)
    printf("%s (%d): %.1f\n", meus_alunos[i].nome, meus_alunos[i].presencas, meus_alunos[i].nota);
    
  return 0;
}

