#include <stdio.h>
int main() {

  int a[2][2], b[2][2], i, j, c[2][2];
  printf("Enter the Elements of A array\n");
  for (i = 0; i < 2; i++) {
    for (j = 0; j < 2; j++)
      scanf("%d", &a[i][j]);
  }
  printf("Enter the Elements of B array\n");
  for (i = 0; i < 2; i++) {
    for (j = 0; j < 2; j++)
      scanf("%d", &b[i][j]);
  }

  for (i = 0; i < 2; i++) {
    for (j = 0; j < 2; j++)
      c[i][j] = a[i][j] + b[i][j];
  }

  for (i = 0; i < 2; i++) {
    printf("\n");
    for (j = 0; j < 2; j++)
      printf("\t%d", c[i][j]);
  }
  return 0;
}