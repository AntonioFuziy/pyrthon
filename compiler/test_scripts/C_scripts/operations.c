#include <stdio.h>

/*função principal do programa*/
int main(){
  /*declaração de variáveis*/
  int i, j;
  int soma, sub, mult, div;

  /*atribuição de valor*/
  i = 10;
  j = 5;

  /*operação de soma*/
  soma = i + j;
  /*operação de subtração*/
  sub = i - j;
  /*operação de multiplicação*/
  mult = i * j;
  /*operação de divisão*/
  div = i / j;

  /*printando valores das operações*/
  printf("%d \n",soma);
  printf("%d \n",sub);
  printf("%d \n",mult);
  printf("%d \n",div);
}

