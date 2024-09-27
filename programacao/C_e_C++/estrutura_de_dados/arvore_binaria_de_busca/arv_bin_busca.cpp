#include <cstdio>
#include <string>

using std::string;

class No
{
    friend class ArvBinBusca; //

public:
    // Construtor do nó
    No(const int chave);

    void escreve(const char *sep = "");

private:
    int chave;
    No *pai;
    No *esq;
    No *dir;
};

class ArvBinBusca
{
public:
    // Construtor da árvore
    ArvBinBusca();
    ArvBinBusca(const ArvBinBusca &outro); // construtor de cópia
    // Destrutor de objetos da classe
    ~ArvBinBusca();

    ArvBinBusca &operator=(const ArvBinBusca &outro); // operador de atribuição

    void escreve_ordenado(); // escreve em percurso em-ordem
    void escreve();

    // Operações básicas
    No *get_raiz();         // devolve a raiz
    No *busca(int k);       // devolve o ponteiro para um elemento, se achar, ou NULL
    No *minimo();           // devolve o menor elemento da árvore
    No *maximo();           // devolve o maior elemento da árvore
    No *sucessor(No *x);    // devolve o sucessor de um elemento
    No *predecessor(No *x); // devolve o predecessor de um elemento

    void insere(int chave);
    bool remove(int chave); // 3 casos

    void limpa(); // remove todos elementos da árvore

private:
    No *raiz;

    void escreve_ordenado(No *x); // escreve em percurso em-ordem
    void escreve(const string &prefixo, No *x);

    No *busca(No *x, int k);    // recebe um ponteiro e uma chave
    No *minimo(No *x);
    No *maximo(No *x);

    void insere(No *z);
    void transplante(No *u, No *v); // substitui a subárvore enraizada em u pela subárvore enraizada em v
    void remove(No *z);

    void limpa(No *x); // dado um nó x, remove recursivamente elementos abaixo e deleta x

    void copia(const ArvBinBusca &T); // copia uma árvore T para a atual a partir da raiz,
                                      // usada no construtor de cópia e no operador de atribuição
    void copia(No *dest, No *orig);   // copia um nó e os descendentes recursivamente
};

int main(void)
{
    ArvBinBusca T; // construtor ArvBinBusca()
    int v[] = {10, 25, 0, 16, 20, 9, 15, 6, 14, 7, 18, 12, 22, 19, 3, 13};
    
    // Insere a chave
    for (const auto &x : v)
        T.insere(x);

    printf("T:\n");
    T.escreve();
    printf("Valores de T em ordem crescente: ");
    T.escreve_ordenado();

    // Impressão da raiz e seus sucessores e predecessores
    No *raiz = T.get_raiz();
    printf("Raiz: ");
    raiz->escreve("\n");

    No *pre = T.predecessor(raiz);
    printf("Predecessor da raiz: ");
    pre->escreve("\n");
    
    No *suc = T.sucessor(raiz);
    printf("Sucessor da raiz: ");
    suc->escreve("\n");

    printf("Sucessor do predecessor da raiz (== raiz): ");
    T.sucessor(pre)->escreve("\n");
    printf("Predecessor do sucessor da raiz (== raiz): ");
    T.predecessor(suc)->escreve("\n");

    No *minimo = T.minimo();
    No *maximo = T.maximo();
    printf("Mínimo: ");
    minimo->escreve("\n");
    printf("Máximo: ");
    maximo->escreve("\n");

    // return 0; // TODO: remover após implementar remoção

    T.remove(0);  // Caso 1:  z tem apenas o filho direito e removemos z para inserir o filho
    T.remove(13); // Caso 2: z tem apenas o filho esquerdo e removemos z para inserir o filho
    T.remove(10); // Caso 3b + 3a: 

    printf("T:\n");
    T.escreve();

    return 0; // TODO: remover após implementar construtor de cópia e operador de atribuição

    ArvBinBusca T2(T); // construtor de cópia
    T2.insere(30);
    printf("T:\n");
    T.escreve();
    printf("T2:\n");
    T2.escreve();

    ArvBinBusca T3 = T; // construtor de cópia
    T3.insere(-8);
    printf("T:\n");
    T.escreve();
    printf("T3:\n");
    T3.escreve();

    T3 = T; // operador de atribuição
    T3.insere(100);
    printf("T:\n");
    T.escreve();
    printf("T3:\n");
    T3.escreve();

    return 0;
}

//***********************************
//*** IMPLEMENTAÇÕES DA CLASSE NO ***
//***********************************

No::No(const int chave) : 
    chave(chave),
    pai(NULL),
    esq(NULL),
    dir(NULL)
{
}

void No::escreve(const char *sep)
{
    printf("%2d%s", chave, sep);
}

//********************************************
//*** IMPLEMENTAÇÕES DA CLASSE ARVBINBUSCA ***
//********************************************

ArvBinBusca::ArvBinBusca()
{
    raiz = NULL;
}

ArvBinBusca::ArvBinBusca(const ArvBinBusca &outro)
{
    copia(outro);
}

// Destrutor de objetos da classe
ArvBinBusca::~ArvBinBusca()
{
    limpa();
}

// Operador de atribuição
ArvBinBusca &ArvBinBusca::operator=(const ArvBinBusca &outro)
{
    limpa();
    copia(outro);
    return *this;
}

// Percurso em ordem
void ArvBinBusca::escreve_ordenado()
{
    escreve_ordenado(raiz);
    putchar('\n');
}

void ArvBinBusca::escreve_ordenado(No *x)
{
    if (x == NULL)
        return;

    escreve_ordenado(x->esq);
    x->escreve(" ");
    escreve_ordenado(x->dir);
}

void ArvBinBusca::escreve()
{
    escreve("", raiz);
}

void ArvBinBusca::escreve(const string &prefixo, No *x)
{
    if (x == NULL)
        return;

    bool ehDireito = x->pai and x->pai->dir == x;
    bool temIrmaoEsq = x->pai and x->pai->esq;

    printf("%s", prefixo.c_str());
    printf(ehDireito and temIrmaoEsq ? "├──" : "└──");

    if (x->pai == NULL) // raiz
        x->escreve("\n");
    else
        x->escreve(ehDireito ? "d\n" : "e\n");

    escreve(prefixo + (ehDireito and temIrmaoEsq ? "│   " : "    "), x->dir);
    escreve(prefixo + (ehDireito and temIrmaoEsq ? "│   " : "    "), x->esq);
}

No *ArvBinBusca::get_raiz()
{
    return raiz;
}

No *ArvBinBusca::busca(int k)
{
    return busca(raiz, k);
}

No *ArvBinBusca::busca(No *x, int k)
{
    if (x == NULL or x->chave == k)
        return x;

    if (k < x->chave)
        return busca(x->esq, k);
    else
        return busca(x->dir, k);
}

No *ArvBinBusca::minimo()
{
    return raiz ? minimo(raiz) : NULL;
}

No *ArvBinBusca::minimo(No *x)
{
    while (x->esq != NULL)
        x = x->esq;
    return x;
}

No *ArvBinBusca::maximo()
{
    return raiz ? maximo(raiz) : NULL;
}

No *ArvBinBusca::maximo(No *x)
{
    while (x->dir != NULL)
        x = x->dir;
    return x;
}

No *ArvBinBusca::sucessor(No *x)
{
    // Se tem filho direito, o sucessor é o mínimo do filho direito
    if (x->dir != NULL)
        return minimo(x->dir);
    // Se não tem filho direito
    No *y = x->pai;
    while (y != NULL and x == y->dir)
    {
        x = y;
        y = y->pai;
    }
    return y;
}

No *ArvBinBusca::predecessor(No *x)
{
    // Se tem filho esquerdo, o predecessor é o máximo do filho esquerdo
    if (x->esq != NULL)
        return maximo(x->esq);

    // Se não tem filho esquerdo, o predecessor é o primeiro ancestral que é filho direito
    No *y = x->pai;
    while (y != NULL and x == y->esq)
    {
        x = y;
        y = y->pai;
    }
    return y;
}

void ArvBinBusca::insere(int chave)
{
    // Cria um novo nó
    No *z = new No(chave);
    // Insere a chave no nó da árvore
    insere(z);
}

void ArvBinBusca::insere(No *z)
{
    No *y = NULL;
    No *x = raiz;

    while (x != NULL)
    {
        y = x;
        if (z->chave < x->chave)
            x = x->esq;
        else
            x = x->dir;
    }
    z->pai = y;
    if (y == NULL)
        raiz = z;
    else if (z->chave < y->chave)
        y->esq = z;
    else
        y->dir = z;
}

void ArvBinBusca::transplante(No *u, No *v)
{
    // TODO: implementar
    if (u->pai == nullptr) {
        raiz = v;
    } else if (u == u->pai->esq) {
        u->pai->esq = v;
    } else {
        u->pai->dir = v;
    }

    if (v != nullptr) {
        v->pai = u->pai;
    }

}
// Valor
bool ArvBinBusca::remove(int chave)
{
    No *z = busca(raiz, chave);
    if (z == NULL)
        return false;

    remove(z);
    delete z;
    return true;
}
// Nó
void ArvBinBusca::remove(No *z)
{
    // TODO: implementar
    // ---- caso 1: z tem apenas o filho direito ou não tem filhos ----
    if (z->esq == nullptr) {
        transplante(z, z->dir);
    } else {
        // ---- caso 2: z tem apenas o filho esquerdo ----
        if (z->dir == nullptr) {
            transplante(z, z->esq);
        } else { // ---- caso 3: z tem dois filhos ----
            No *y = minimo(z->dir);
            if (y->pai != z) {
                // e o sucessor é o filho direito de alguém  
                transplante(y, y->dir);
                y->dir = z->dir;
                y->dir->pai = y;
            }
            // e o sucessor é o filho esquerdo de alguém
            transplante(z, y);
            y->esq = z->esq;
            y->esq->pai = y;
        };
    };
}

void ArvBinBusca::limpa()
{
    limpa(raiz);
    raiz = NULL;
}

void ArvBinBusca::limpa(No *x)
{
    // TODO: implementar
    if (x != nullptr){
        // Percorre em Pós-ordem
        limpa(x->esq);
        limpa(x->dir);
        delete x;
    }
}

void ArvBinBusca::copia(const ArvBinBusca &T)
{
    if (T.raiz == NULL)
        raiz = NULL;
    else
    {
        raiz = new No(T.raiz->chave);
        copia(raiz, T.raiz);
    }
}

void ArvBinBusca::copia(No *dest, No *orig)
{
    // TODO: implementar
}
