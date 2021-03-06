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


//_______________________________________A C H A  O  M I N I M O_______________________________________
//encontra o minimo; retorna a celula.
celula procurar_minimo(celula *lst){
  celula *var, *minimo;
  int menor;
  menor = lst->seg->conteudo;
  for(var=lst->seg;var->seg!=NULL;var=var->seg){
    if(var->conteudo < menor){
      menor = var->conteudo;
      lst = var;
    }
  }
  if(var->conteudo < menor){
    menor = var->conteudo;
    lst = var;
  }
  return *lst;
}

//versao recursiva
celula procura_minimo_recursivo(celula *minima, celula *lst){
  if(minima->conteudo > lst->conteudo){
    minima = lst;
  }
  if(lst->seg == NULL){
    return *minima;
  }
  return procura_minimo_recursivo(minima, lst->seg);
}


//_______________________________________I N V E R S A O_______________________________________
//inverte uma lista.
void inverter_lista(celula *lst){
	
}
