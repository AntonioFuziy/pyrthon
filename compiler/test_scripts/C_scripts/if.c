#include <stdio.h>


int main(){
  int i, j, k;
  i = 10;
  j = 5;
  
  /*compara se i > j*/
  if(i > j){
    k = i;
    printf("i maior que j \n");
  } /*se i <= j*/  
  else {
    k = j;
    printf("j maior que i \n");
  }
  printf("%d \n", k);
}

