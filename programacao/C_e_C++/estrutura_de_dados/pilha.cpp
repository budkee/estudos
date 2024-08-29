#include <stdio.h>

//  ----------------- Classes ----------------- 
class Celula 
{
  friend class Pilha; // Acessa os membros privados e protegidos de Celula

public: // Membros públicos de Celula

  void escrever (const char *sep =", "); // Imprime uma lista de elementos separados por vírgula
  
  Celula(int chave); // Construtor de instâncias de Celula com parâmetros iniciais
  Celula(); // Construtor de instâncias de Celula sem parâmetros iniciais

private: // Membros privados de Celula, só podem ser acessados dentro da própria classe ou por uma classe amiga, como a Pilha
  int chave;  // Equivale ao i da propriedade
  Celula *prox; // Ponteiro apontando para próxima instância da Celula

};

class Pilha
{

public:

  void empilhar(int chave); // Empilha elementos na Pilha a partir da sua chave
  int desempilhar (void); // Atualiza o topo e retorna o valor da chave do elemento removido
  void escrever (void); // Escreve o conteúdo atual da pilha
  bool vazia (void); // Verifica se a pilha está vazia
  
  Pilha (); // Construtor
  ~Pilha(); // Destrutor

private:

  Celula *topo; // Ponteiro apontando pro topo, que no início é nulo (aponta para nullptr)

};

//  ----------------- Definições e Métodos das Classes ----------------- 

// 1. Construtor da Celula
Celula::Celula(int chave)
{
  this->chave = chave;
  this->prox = NULL;
}
// Definição da cabeça da Celula
Celula::Celula()
{
  this->prox = NULL;
}
/* // Posso fazer o construtor dessa forma...
   Celula::Celula(int chave) :
   chave(chave);
   prox(NULL);
   {
   //posso fazer outras coisas aqui, outros comandos.
   }
*/

// 1.1 Métodos da Celula
void Celula::escrever (const char *sep) // Identifica o separador que será impresso após escrever o valor da chave
{
  printf("%d%s", this->chave, sep);
}

// 2. Construtor da Pilha
Pilha::Pilha ()
{
  topo = new Celula(); // Conjunto de celulas
}

Pilha::~Pilha ()
{
  /*
    Celula *p = topo->prox;

    while (p != NULL)
    {
    delete topo;
    topo = p;
    p = p->prox;
    }
    delete topo;
  */

  while(!vazia())
    desempilhar();
  delete topo;

}

// 2.1 Métodos da Pilha
void Pilha::empilhar (int chave)
{
  Celula *c = new Celula(chave);

  c->prox = topo->prox;
  topo->prox = c;
}

int Pilha::desempilhar (void)
{
  int chave;
  Celula *p;

  p = topo->prox;

  topo->prox = p->prox;

  chave = p->chave;
  delete p;

  return chave;
}

void Pilha::escrever (void)
{
  Celula *p;

  for (p = topo->prox; p!= NULL; p = p->prox)
    if (p->prox == NULL)
      p->escrever("\n");
    else
      p->escrever();
}

bool Pilha::vazia (void)
{
  return topo->prox == NULL ? true : false;
}

// ----------------- Módulo principal ----------------- 
int main (void)
{
  // Intancio uma pilha p
  Pilha p;

  // Adiciono valores às celulas da pilha p
  p.empilhar(2);
  p.empilhar(4);
  p.empilhar(3);
  p.escrever();

  printf("A chave desempilhada foi: %d.\n", p.desempilhar());
  p.escrever();

  return 0;
}
// ----------------- EOF ----------------- 