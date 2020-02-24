/*Ponteiros em C são de baixo nivel, sao muito perigosos.
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
         printf ("%d ", p->conteudo);
     printf("\n");
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

/*13) CONCATENAÇÃO.
Escreva uma função que concatene
duas listas encadeadas (isto é, “amarre” a segunda no
fim da primeira)*/

/*18) LIBERAÇÃO. Escreva uma função que aplique a função
free
a todas as células de uma lista encadeada.
Estamos supondo, é claro, que cada célula da lista foi
originalmente alocada por
malloc.*/

void questao9(){//___________________________________________________________________________________________________
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




void questao13(){//___________________________________________________________________________________________________
  int a;
  //craindo duas listas encadeadas
    celula *lst, *lst2;
    lst = malloc(sizeof(celula));
    lst2 = malloc(sizeof(celula));
    lst->seg = NULL; lst2->seg = NULL;
    for (a=0;a<10;a++){
      Insere(a, lst);
      Insere((a), lst2);
    }
  //---------------------------------
  celula *p;//GET ULTIMO PONTEIRO 
  p = lst->seg;
  while(p->seg!=NULL){
      p = p->seg;
  }
  p->seg = lst2->seg;
  Imprima(lst);
  
}


void questao18(){//___________________________________________________________________________________________________
  int a;
  celula *lst;
  lst = malloc(sizeof(celula));
  lst->seg = NULL;
  for(a=5;a>0;a--){
    Insere(a, lst);
  }
  celula *var;
  celula *p;
  p = lst->seg;
  while(p->seg != NULL){
    var = p->seg;
    free(p);
    p = var;
  }
  var = p->seg;
  free(p);
  p = var;
  free(lst);
}


void questao4(){
  int a;
  celula *lst;
  lst = malloc(sizeof(celula));
  lst->seg = NULL;
  for(a=10;a<50;a++){
    Insere(a, lst);
  }
  celula *p;
  p=lst;
  int maior, menor;
  menor = lst->conteudo;
  maior = lst->conteudo;
  while(p->seg != NULL){
    if(p->conteudo < menor) menor = p->conteudo;
    else if(p->conteudo > maior) maior = p->conteudo;
    p=p->seg;
  }
  if(p->conteudo < menor) menor = p->conteudo;
  else if(p->conteudo > maior) maior = p->conteudo;
  printf("%d %d \n", maior, menor);
}
void questa4recursiva(celula *p){
  int a;
  celula *lst;
  lst = malloc(sizeof(celula));
  lst->seg = NULL;
  for(a=10;a<50;a++){
    Insere(a, lst);
  }
  
  p=lst;
  int maior, menor;
  menor = lst->conteudo;
  maior = lst->conteudo;
  if(p->seg == NULL){
    printf("%d %d\n", maior, menor);
    
  }
  else{

  }
}
int main(){
  //questao9();
  //questao13();
  //questao18();
  questao4();
  return 0;    
}
