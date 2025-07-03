#include <cstdio>
#include <string>

using std::string;

class No {
  friend class AVL;
  
public:
  No(const int chave);

  void escreve(const char *sep = "");
  inline bool eh_raiz();         // devolve true se o nó é raiz
  inline bool eh_direito();      // devolve true se o nó é filho direito do seu pai
  inline bool eh_esquerdo();     // devolve true se o nó é filho esquerdo do seu pai
  inline int bal();              // calcula e devolve o fator de balanceamento
  inline void atualiza_altura(); // recalcula a altura a partir das alturas dos filhos
  
private:
  int chave;
  int altura; // consideramos que a altura das folhas é 0
  No *pai;
  No *esq;
  No *dir;
};


class AVL
{
public:
  AVL();
  AVL(const AVL& outro); // construtor de cópia
  ~AVL();
  AVL& operator=(const AVL& outro); // operador de atribuição
  
  void escreve_ordenado(); // escreve em percurso em-ordem
  void escreve();

  No *get_raiz();         // devolve a raiz
  No *busca(int k);       // devolve o ponteiro para um elemento, se achar, ou NULL
  No *minimo();           // devolve o menor elemento da árvore
  No *maximo();           // devolve o maior elemento da árvore
  No *sucessor(No *x);    // devolve o sucessor de um elemento
  No *predecessor(No *x); // devolve o predecessor de um elemento

  void insere(int chave); // insere uma chave
  bool remove(int chave); // remove uma árvore

  void limpa(); // remove todos elementos da árvore
  
private:
  No *raiz;

  void escreve_ordenado(No *x); // escreve em percurso em-ordem
  void escreve(const string& prefixo, No *x);
  
  No *busca(No *x, int k); // chamada recursiva inicial para a raiz
  No *minimo(No *x);       // devolve o mínimo a partir de um nó
  No *maximo(No *x);       // devolve o máximo a partir de um nó
  
  // recalcula balanceamento e rotaciona, se necessário, devolvendo o
  // ponteiro para o nó que ocupou a posição de p na árvore (caso uma
  // rotação tenha sido realizada)
  No *ajusta_balanceamento(No *p, bool ins);
  
  void transplante(No *u, No *v);  // transplante de v para u, não altera filhos
  void insere(No *z);              // insere um nó z na árvore
  void remove(No *z);              // remove um nó z da árvore
  
  void limpa(No *x); // dado um nó x, remove recursivamente todos elementos abaixo e deleta x
  
  void copia(const AVL& T); // copia uma árvore T para a atual a partir da raiz,
                            // usada no construtor de cópia e no operador de atribuição
  void copia(No *dest, No *orig); // copia um nó e os descendentes recursivamente
  
public: // TODO: remover esta linha após testar rotações na main
  void rotacao_dir(No *p); // Rotação à direita: p e p->esq
  void rotacao_esq(No *p); // Rotação à esquerda: p e p->dir
  void rotacao_dupla_dir(No *p); // Rotação dupla à direita: p->esq e p->esq->dir à esquerda, então p e p->esq à direita
  void rotacao_dupla_esq(No *p); // Rotação dupla à esquerda: p->dir e p->dir->esq à direita, então p e p->dir à esquerda
};


int main(void)
{
  AVL T; // construtor AVL()
  //  int v[] = {10, 25, 0, 16, 20, 9, 15, 6, 14, 7, 18, 12, 22, 19, 3, 13, 28};
  int v[] = {20, 23, 18, 16, 19, 15, 17, 22, 14};

  printf("##INSERÇÕES##\n\n");
  printf("T:\n");
  for (const auto &x : v) {
    printf("\nInserindo %d...\n", x);
    T.insere(x); // Inicialmente, sem balanceamento
    printf("T:\n");
    T.escreve();
  }

  //printf("\n##TESTE DE ROTAÇÕES##\n\n");
  //No *raiz = T.get_raiz();
  //T.rotacao_esq(raiz);
  //T.escreve();
  //raiz = T.get_raiz(); // a raiz agora é outra, precisamos obtê-la novamente
  //T.rotacao_dir(raiz);
  //T.escreve();
  // TODO: após testar rotações, torne funções de rotação *privadas*

  printf("\n##REMOÇÕES##\n\n");
  printf("T:\n");
  T.escreve();
  for (const auto &x : v) {
    printf("\nRemovendo %d...\n", x);
    T.remove(x);
    printf("T:\n");
    T.escreve();
  }
  
  return 0;
}


//***********************************
//*** IMPLEMENTAÇÕES DA CLASSE NO ***
//***********************************

No::No(const int chave) :
  chave(chave),
  altura(0),
  pai(NULL),
  esq(NULL),
  dir(NULL) {
}

void No::escreve(const char *sep) {
  printf("%2d(%d)%s", chave, bal(), sep);
}

bool No::eh_raiz() {
  return pai == NULL;
}

bool No::eh_direito() {
  return !eh_raiz() and pai->dir == this;
}

bool No::eh_esquerdo() {
  return !eh_raiz() and pai->esq == this;
}

int No::bal() {
  int alt_esq = esq ? esq->altura : -1;
  int alt_dir = dir ? dir->altura : -1;
  return alt_esq - alt_dir;
}

void No::atualiza_altura() {
  int alt_esq = esq ? esq->altura : -1;
  int alt_dir = dir ? dir->altura : -1;
  altura = 1 + (alt_esq > alt_dir ? alt_esq : alt_dir);
}


//************************************
//*** IMPLEMENTAÇÕES DA CLASSE AVL ***
//************************************

AVL::AVL() {
  raiz = NULL;
}

AVL::AVL(const AVL& outro) {
  copia(outro);
}

AVL::~AVL() {
  limpa();
}

AVL& AVL::operator=(const AVL& outro) {
  limpa();
  copia(outro);
  return *this;
}

void AVL::escreve_ordenado() {
  escreve_ordenado(raiz);
  putchar('\n');
}

void AVL::escreve_ordenado(No *x) {
  // percurso em-ordem
  if (x == NULL)
    return;
  
  escreve_ordenado(x->esq);
  x->escreve(" ");
  escreve_ordenado(x->dir);
}

void AVL::escreve() {
  escreve("", raiz);
}

void AVL::escreve(const string& prefixo, No *x) {
  if (x == NULL)
    return;

  bool ehDireito = x->pai and x->pai->dir == x;
  bool temIrmaoEsq = x->pai and x->pai->esq;
  
  printf(prefixo.c_str());
  printf(ehDireito and temIrmaoEsq ? "├──" : "└──" );

  if (x->pai == NULL) // raiz
    x->escreve("\n");
  else
    x->escreve(ehDireito ? "d\n" : "e\n");
  
  escreve(prefixo + (ehDireito and temIrmaoEsq ? "│   " : "    "), x->dir);
  escreve(prefixo + (ehDireito and temIrmaoEsq ? "│   " : "    "), x->esq);
}

No *AVL::get_raiz() {
  return raiz;
}

No *AVL::busca(int k) {
  return busca(raiz, k);
}

No *AVL::busca(No *x, int k) {
  if (x == NULL or k == x->chave)
    return x;

  if (k < x->chave)
    return busca(x->esq, k);
  else
    return busca(x->dir, k);
}

No *AVL::minimo() {
  return raiz ? minimo(raiz) : NULL;
}

No *AVL::minimo(No *x) {
  while (x->esq != NULL)
    x = x->esq;
  return x;
}

No *AVL::maximo() {
  return raiz ? maximo(raiz) : NULL;
}

No *AVL::maximo(No *x) {
  while (x->dir != NULL)
    x = x->dir;
  return x;
}

No *AVL::sucessor(No *x) {
  if (x->dir != NULL)
    return minimo(x->dir);

  No *y = x->pai;
  while (y != NULL and x == y->dir) {
    x = y;
    y = y->pai;
  }
  return y;
}

No *AVL::predecessor(No *x) {
  if (x->esq != NULL)
    return maximo(x->esq);

  No *y = x->pai;
  while (y != NULL and x == y->esq) {
    x = y;
    y = y->pai;
  }
  return y;
}

No *AVL::ajusta_balanceamento(No *p, bool ins) {
  
  p->atualiza_altura();
  
  if (p->bal() == 2) {        // Caso 1
    if (p->esq->bal() >= 0) { // Caso 1.1
      if (ins)
	printf(">> Rotação direita (Caso 1.1)\n");
      rotacao_dir(p);
    }
    else {                    // Caso 1.2
      if (ins)
	printf(">> Rotação dupla direita (Caso 1.2)\n");
      rotacao_dupla_dir(p);
    }
    p = p->pai;               // após a rotação p desceu 1 nível, precisamos subir de volta
  }
  else if (p->bal() == -2) {  // Caso 2
    if (p->dir->bal() <= 0) { // Caso 2.1
      if (ins)
	printf(">> Rotação esquerda (Caso 2.1)\n");
      rotacao_esq(p);
    }
    else {                    // Caso 2.2
      if (ins)
	printf(">> Rotação dupla esquerda (Caso 2.2)\n");
      rotacao_dupla_esq(p);
    }
    p = p->pai;              // após a rotação p desceu 1 nível, precisamos subir de volta
  }
  
  return p;
}

void AVL::insere(int chave) {
  No *z = new No(chave);
  insere(z);
}

void AVL::insere(No *z) {
  No *y = NULL;
  No *x = raiz;

  while (x != NULL) {
    y = x;
    x = z->chave < x->chave ? x->esq : x->dir;
  }
  z->pai = y;
  if (y == NULL)
    raiz = z;
  else
    if (z->chave < y->chave)
      y->esq = z;
    else
      y->dir = z;

  // Atualização dos fatores de balanceamento
  if (z->eh_raiz())
    return;
  
  do { // o laço inicia subindo imediatamente para o pai do nó inserido
    z = z->pai;
    z = ajusta_balanceamento(z, true);
  } while (!z->eh_raiz() and z->bal() != 0);
}

void AVL::transplante(No *u, No *v) {
  if (u->eh_raiz())
    raiz = v;
  else
    if (u->eh_esquerdo())
      u->pai->esq = v;
    else
      u->pai->dir = v;

  if (v != NULL)
    v->pai = u->pai;
}

bool AVL::remove(int chave) {
  No *z = busca(raiz, chave);
  if (z == NULL)
    return false;

  remove(z);
  delete z;
  return true;
}

void AVL::remove(No *z) {

  // Precisamos salvar a posição na qual a árvore foi efetivamente
  // modificada e onde devemos começar a atualização de
  // alturas/fatores de balanceamento.
  No *p = NULL;
  
  if (z->esq == NULL) { // 1o caso

    p = z->pai; // a altura de z->dir (que substituirá z) não será alterada, e z->dir pode ser nulo
    transplante(z, z->dir);
  }
  else {
    if (z->dir == NULL) { // 2o caso
      printf("<< Remoção 2o caso\n");
      p = z->pai; // a altura de z->esq (que substituirá z) não será alterada
      transplante(z, z->esq);
    }
    else { // 3o caso
      No *y = minimo(z->dir);
      
      printf("<< Remoção 3o caso (a) ");
      if (y->pai != z) { // (b)
	printf("+ (b)\n");
        p = y->pai; // a altura de y->dir (que substituirá y) não será alterada, e y->dir pode ser nulo
        transplante(y, y->dir); 
        y->dir = z->dir;
        y->dir->pai = y;
      }
      printf("\n");
      
      transplante(z, y); // (a)
      y->esq = z->esq;
      y->esq->pai = y;

      // Se não entramos no caso 3(b), a atualização de "p" é um
      // pouco diferente dos outros casos. Se entramos diretamente no
      // caso 3(a), o nó "z" removido tem filhos esquerdo E direito,
      // mas o sucessor "y" que o substituirá é seu filho direito. A
      // altura de "y" *PODE* ser modificada, já que "y" terá um filho
      // esquerdo que não tinha antes (o antigo filho esquerdo de "z").
      if (p == NULL) // se fomos direto pro caso 3(a) sem entrar no caso 3(b)
        p = y;
    }
  }

  // Atualização das alturas/fatores de balanceamento

  // Se p é nulo, significa que a raiz foi removida e substituída por
  // seu único filho, então nada muda.
  if (p == NULL)
    return;
  
  // Não podemos subir imediatamente para o pai de p (como na
  // inserção), pois p é o próprio nó que precisa atualização.
  p = ajusta_balanceamento(p, false);
 
  while (!p->eh_raiz() and p->bal() != 1 and p->bal() != -1) { 
    p = p->pai;
    p = ajusta_balanceamento(p, false);
  }
}

void AVL::limpa() {
  limpa(raiz);
  raiz = NULL;
}

void AVL::limpa(No *x) {
  if (x == NULL)
    return;

  limpa(x->esq);
  limpa(x->dir);
  delete x;
}

void AVL::copia(const AVL& T) {
  if (T.raiz == NULL)
    raiz = NULL;
  else {
    raiz = new No(T.raiz->chave);
    copia(raiz, T.raiz);
  }
}

void AVL::copia(No *dest, No *orig) {
  if (orig->esq) {
    dest->esq = new No(orig->esq->chave);
    dest->esq->pai = dest;
    copia(dest->esq, orig->esq);
  }
  
  if (orig->dir) {
    dest->dir = new No(orig->dir->chave);
    dest->dir->pai = dest;
    copia(dest->dir, orig->dir);
  }
}

void AVL::rotacao_dir(No *p) {
  No *u = p->esq;
  // arruma u e seu pai (o pai de p)
  transplante(p, u);
  // move p para a direita de u, e o filho direito de u para a esquerda de p
  p->pai = u;
  p->esq = u->dir;
  u->dir = p;
  if (p->esq) p->esq->pai = p;
  // atualiza alturas
  p->atualiza_altura();
  u->atualiza_altura();
}

void AVL::rotacao_esq(No *p) {
  No *u = p->dir;
  // arruma u e seu pai (o pai de p)
  transplante(p, u);
  // move p para a esquerda de u, e o filho esquerdo de u para a direita de p
  p->pai = u;
  p->dir = u->esq;
  u->esq = p;
  if (p->dir) p->dir->pai = p;
  // atualiza alturas
  p->atualiza_altura();
  u->atualiza_altura();
}

void AVL::rotacao_dupla_dir(No *p) {
  rotacao_esq(p->esq);
  rotacao_dir(p);
}

void AVL::rotacao_dupla_esq(No *p) {
  rotacao_dir(p->dir);
  rotacao_esq(p);
}
