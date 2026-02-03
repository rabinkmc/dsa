#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int i;
  char c;
  double d;
  char a[];
} Node;

Node *NewNode() {
  Node *node = malloc(sizeof(Node));
  node->i = 0;
  node->d = 0;
  return node;
}
int main(void) {
  Node *node = NewNode();
  printf("offsets: i=%zu; c=%zu; d=%zu; a=%zu\n", offsetof(Node, i),
         offsetof(Node, c), offsetof(Node, d), offsetof(Node, a));
  printf("sizeof(Node) = %zu\n", sizeof(Node));
  return 0;
}
