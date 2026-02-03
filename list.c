#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct Lnode {
        int val;
        struct Lnode *next;
} Lnode;

Lnode *new_node(int val) {
    Lnode *node = (Lnode *)malloc(sizeof(Lnode));
    node->val = val;
    node->next = NULL;
    return node;
}

void pprint(Lnode *node) {
    if (node == NULL) return;
    printf("%d->", node->val);
    pprint(node->next);
}

Lnode *new_list(int max_val) {
    // from the end
    /*Lnode *node = NULL;*/
    /*for (int i = max_val; i > 0; i--) {*/
    /*    Lnode *tmp = node;*/
    /*    node = new_node(i);*/
    /*    node->next = tmp;*/
    /*}*/
    /*return node;*/

    // this is the standard way
    Lnode dummy;
    dummy.next = NULL;
    Lnode *tail = &dummy;

    for (int i = 1; i <= max_val; i++) {
        tail->next = new_node(i); // dummy.next = 1, 1.next = 2, 2.next = 3
        tail = tail->next;        // tail = 1, 2, 3
    }
    return dummy.next;
}

int rand_int(int min, int max) {
    return min + rand() % (max - min + 1);
}

Lnode *delete_node(Lnode *list, int target) {
    Lnode dummy = {.next = list};
    Lnode *prev = &dummy;
    Lnode *curr = list;
    while (curr != NULL) {
        if (curr->val == target) {
            if (prev != NULL) {
                prev->next = curr->next;
                free(curr);
                break;
            }
            return list;
        }
        prev = curr;
        curr = curr->next;
    }
    return dummy.next;
}

Lnode *insert(Lnode *list, int pos) {
    Lnode dummy = {.next = list};
    Lnode *prev = &dummy;
    Lnode *curr = list;
    while (curr != NULL) {
        if (curr->val == pos) {
            if (prev != NULL) {
                prev->next = curr->next;
                free(curr);
                break;
            }
            return list;
        }
        prev = curr;
        curr = curr->next;
    }
    return dummy.next;
}

int main() {
    /*srand(time(NULL));*/
    Lnode *list = new_list(10);
    /*int dnode = rand_int(1, 10);*/
    /*printf("delete node: %d\n", dnode);*/
    // delete dnode
    list = delete_node(list, 1);
    pprint(list);
}
