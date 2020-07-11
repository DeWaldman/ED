// Quando se tem um vetor e se trabalha com inserçaõ/remoção o pior caso aparece na primeira posição; 
// Caso insira algo na primeira posição todo o vetor sera "arrastado" para a direita;
// caso remova algo na primeira posição todo o vetor sera "arrastado" para a esquerda

// é possivel criar listas com ponteiros;
// diferença entre lista com cabeça e sem cabeça:


//______________________________COM cabeça______________________________________________________
#include <stdio.h>
#include <stdlib.h>

struct cel {
       int conteudo;
       struct cel *seg; /* seguinte */
};

typedef struct cel celula;

void Imprima (celula *lst) {
     celula *p;
     for (p = lst->seg; p != NULL; p = p->seg)
         printf ("%d\n", p->conteudo);
}

void Insere(int y, celula *p){
    celula *nova;
    nova = malloc(sizeof(celula));
    nova->conteudo = y;
    nova->seg = p->seg;
    p->seg = nova;
}

int main(void){
    int i;
    celula *lst;
    lst = malloc(sizeof(celula));
    lst->seg = NULL;

    for (i = 0; i < 10; i++)
        Insere(i, lst);
    Imprima(lst);
    system("pause");
}




//______________________________SEM cabeça______________________________________________________

#include <stdio.h>
#include <stdlib.h>

struct cel {
       int conteudo;
       struct cel *seg; /* seguinte */
};

typedef struct cel celula;

void Imprima2(celula *lst) {
     celula *p;
     for (p = lst; p != NULL; p = p->seg)
         printf ("%d\n", p->conteudo);
}

void Insere2(int y, celula **p){
    celula *nova;
    nova = malloc(sizeof(celula));
    nova->conteudo = y;

    if (*p == NULL) {
        *p = nova;
        nova->seg = NULL;
    } else {
        nova->seg = *p;
        *p = nova;
    }
}

int main(void){
    int i;
    celula *lst; // int a    int *
    lst = NULL;

    for (i = 0; i < 10; i++)
        Insere2(i, &lst);
    Imprima2(lst);
    system("pause");
}
