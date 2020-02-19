/*Ponteiros em C são de baixo nivel, e muito perigosos.
"Programar e C é como dançar num salão muito encerado,
com um monte de facas na mão.*/

#include <stdio.h>
#include <stdlib.h>
struct cel {
       int conteudo;
       struct cel *seg; /* seguinte */
};typedef struct cel celula;

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


//___________________________________________Q U E S T O E S___________________________________________
/*9) VETOR PARA LISTA.
Escreva uma função que copie um
vetor para uma lista encadeada*/
void questao9(){
  int a;
  int vetor[6] = {4, 8, 15, 16, 23, 42};
  celula *lst;
  lst = malloc(sizeof(celula));
  lst->seg = NULL;
  for(a=5;a>0;a--){
    Insere(vetor[a], lst);
  }
  Imprima(lst);
}

/*13) CONCATENAÇÃO.
Escreva uma função que concatene
duas listas encadeadas (isto é, “amarre” a segunda no
fim da primeira)*/
void questao13(){
  int a;
  //craindo duas listas encadeadas
    celula *lst, *lst2;
    lst = malloc(sizeof(celula));
    lst2 = malloc(sizeof(celula));
    lst->seg = NULL; lst2->seg = NULL;
    for (a=0;a<10;a++){
      Insere(a, lst);
	  Insere((a+1), lst2);
	}
  //---------------------------------
  
  Imprima(lst);
  
}
int main(){
  questao9();
  questao13();

  return 0;	
}
