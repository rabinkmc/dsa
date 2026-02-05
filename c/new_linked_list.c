#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
        int val;
        struct Node *next;
} Node;

typedef struct MyLinkedList {
        Node *head;
        Node *tail;
        int size;
} MyLinkedList;

Node *new_node(int val) {
    Node *node = (Node *)malloc(sizeof(Node));
    node->val = val;
    node->next = NULL;
    return node;
}

MyLinkedList *myLinkedListCreate() {
    MyLinkedList *list = (MyLinkedList *)malloc(sizeof(MyLinkedList));
    Node *dummy = new_node(-1);
    list->head = dummy;
    list->tail = dummy;
    list->size = 0;
    return list;
}

int myLinkedListGet(MyLinkedList *obj, int index) {
    if (index < 0 || index >= obj->size) return -1;

    Node *curr = obj->head->next;
    for (int i = 0; i < index; i++) curr = curr->next;
    return curr->val;
}

void myLinkedListAddAtHead(MyLinkedList *obj, int val) {
    Node *node = new_node(val);
    node->next = obj->head->next;
    obj->head->next = node;

    if (obj->tail == obj->head) {
        obj->tail = node;
    }
    obj->size++;
}

void myLinkedListAddAtTail(MyLinkedList *obj, int val) {
    Node *node = new_node(val);
    obj->tail->next = node;
    obj->tail = node;
    obj->size++;
}

void myLinkedListAddAtIndex(MyLinkedList *obj, int index, int val) {
    if (index > obj->size) return;
    if (index < 0) index = 0;

    Node *prev = obj->head;
    for (int i = 0; i < index; i++) prev = prev->next;

    Node *node = new_node(val);
    node->next = prev->next;
    prev->next = node;

    if (prev == obj->tail) {
        obj->tail = node;
    }
    obj->size++;
}

void myLinkedListDeleteAtIndex(MyLinkedList *obj, int index) {
    if (index < 0 || index >= obj->size) return;

    Node *prev = obj->head;
    for (int i = 0; i < index; i++) prev = prev->next;

    Node *curr = prev->next;
    prev->next = curr->next;

    if (curr == obj->tail) {
        obj->tail = prev;
    }

    free(curr);
    obj->size--;
}

void myLinkedListFree(MyLinkedList *obj) {
    Node *curr = obj->head;
    while (curr) {
        Node *tmp = curr;
        curr = curr->next;
        free(tmp);
    }
    free(obj);
}

int main() {
    MyLinkedList *obj = myLinkedListCreate();
    myLinkedListAddAtHead(obj, 1);
    myLinkedListAddAtTail(obj, 3);
    myLinkedListAddAtIndex(obj, 1, 2);
    printf("val: %d\n", myLinkedListGet(obj, 1));
    myLinkedListDeleteAtIndex(obj, 1);
    printf("val: %d\n", myLinkedListGet(obj, 1));
    return 0;
}
