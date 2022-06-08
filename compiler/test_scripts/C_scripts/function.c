#include <stdio.h>



/*função de soma*/
int soma(int x, int y){
  int z;
  z = x + y;
  return z;
}

/*função de subtração*/
int sub(int x, int y){
  int z;
  z = x - y;
  return z;
}

int main(){
  int i, j;
  i = 10;
  j = 5;
  int sum, subt;
  /*chamada da função de soma*/
  sum = soma(i, j);
  /*chamada da função de subtração*/
  subt = sub(i, j);
  printf("%d \n", sum);
  printf("%d \n", subt);
}

