#include <stdio.h>


int main(){
  int i, n, k;
  k = 1;
  i = 0;
  n = 5;
  
  /*enquanto i < n*/
  while(i < n){
    printf("%d \n", i);
    k = k * 10;
    printf("%d \n", k);
    i = i + 1;
  }
  printf("fim \n");
}

