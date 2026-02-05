#include <stdlib.h>
#include <stdio.h>

struct ListNode {
        int val;
        struct ListNode *next;
};

struct ListNode *new_node(int val, struct ListNode *next) {
    struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = next;
    return node;
}

struct ListNode *removeElements(struct ListNode *head, int val) {
    struct ListNode dummy = {.next = head};
    struct ListNode *prev = &dummy;
    struct ListNode *curr = head;
    while (curr) {
        if (curr->val == val) {
            prev->next = curr->next;
            free(curr);
            curr = prev->next;
        } else {
            prev = curr;
            curr = curr->next;
        }
    }
    return dummy.next;
}

void pprint(struct ListNode *node) {
    if (node == NULL) return;
    printf("%d->", node->val);
    pprint(node->next);
}

int main() {
    struct ListNode *six2 = new_node(6, NULL);
    struct ListNode *five = new_node(5, six2);
    struct ListNode *four = new_node(4, five);
    struct ListNode *three = new_node(3, four);
    struct ListNode *six = new_node(6, three);
    struct ListNode *two = new_node(2, six);
    struct ListNode *one = new_node(1, two);

    struct ListNode *list = removeElements(one, 6);
    pprint(list);
    return 0;
}
