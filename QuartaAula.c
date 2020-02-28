/*Ponteiros em C são de baixo nivel e muito perigosos.
"Programar e C é como dançar num salão muito encerado,
com um monte de facas na mão.*/

#include <stdio.h>
#include <stdlib.h>

//_______________________________________E S T R U T U R A  B A S E_______________________________________
struct cel {
  int conteudo;
  struct cel *seg; /* seguinte */
};typedef struct cel celula;

void Insere(int y, celula *p){
  celula *nova;     
  nova = malloc(sizeof(celula));    
  nova->conteudo = y; 
  nova->seg = p->seg; 
  p->seg = nova; 
}

void Imprima (celula *lst) {
  celula *p;
  for (p=lst->seg;p!=NULL;p=p->seg)
    printf ("%d, ", p->conteudo);
  printf("\n");
}


//_______________________________________V E T O R  P A R A  L I S T A_______________________________________
//Recebe um vetor, retorna uma lista encadeada.
celula vetor_para_lista(int *vetor){
  int a;
	celula *lst;
  lst = malloc(sizeof(celula));
  lst->seg = NULL;
  for(a=5;a>0;a--){
    Insere(vetor[a], lst);
  }
	return lst;
}


//_______________________________________C O N C A T E N A C A O_______________________________________
//concatena duas listas; concatena a em b.
void concatenar_listas(celula *a, celula *b){
	celular *var;
	var=b->seg;
	while(var!=NULL){
	  var=var->seg;
	}
	var->seg = a;
}


//_______________________________________L I B E R A C A O_______________________________________
//libera (deleta) uma lista encadeada.
void deletar_lista(celula *lst){
	celula *var;
  celula *p;
  p = lst->seg;
  while(p->seg!=NULL){
    var = p->seg;
    free(p);
    p = var;
  }
  var = p->seg;
  free(p);
  p = var;
  free(lst);
}
