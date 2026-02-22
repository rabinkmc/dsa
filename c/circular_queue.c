#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
typedef struct LinkedList {
        int value;
        struct LinkedList *next;
} LinkedList;

typedef struct {
        LinkedList *head;
        LinkedList *tail;
        int size;
        int capacity;
} MyCircularQueue;

MyCircularQueue *myCircularQueueCreate(int k) {
    MyCircularQueue *obj = malloc(sizeof(MyCircularQueue));
    obj->head = NULL;
    obj->tail = NULL;
    obj->capacity = k;
    obj->size = 0;
    return obj;
}

LinkedList *linkedlist_new(int value) {
    LinkedList *obj = malloc(sizeof(LinkedList));
    obj->value = value;
    obj->next = NULL;
    return obj;
}

bool myCircularQueueEnQueue(MyCircularQueue *obj, int value) {
    if (obj->size == obj->capacity) {
        return false;
    }
    // insert element in the queue;
    LinkedList *ll = linkedlist_new(value);
    if (obj->size == 0) {
        obj->head = obj->tail = ll;
        ll->next = ll;
    } else {
        ll->next = obj->head;
        obj->tail->next = ll;
        obj->tail = ll;
    }
    obj->size++;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue *obj) {
    if (obj->size == 0) {
        return false;
    }
    if (obj->size == 1) {
        free(obj->head);
        obj->head = obj->tail = NULL;
        obj->size = 0;
        return true;
    }
    LinkedList *tmp = obj->head;
    obj->head = tmp->next;
    free(tmp);
    obj->tail->next = obj->head;
    obj->size--;
    return true;
}

int myCircularQueueFront(MyCircularQueue *obj) {
    if (obj->size == 0) {
        return -1;
    }
    return obj->head->value;
}

int myCircularQueueRear(MyCircularQueue *obj) {
    if (obj->size == 0) {
        return -1;
    }
    return obj->tail->value;
}

bool myCircularQueueIsEmpty(MyCircularQueue *obj) {
    return obj->size == 0;
}

bool myCircularQueueIsFull(MyCircularQueue *obj) {
    return obj->size == obj->capacity;
}

void myCircularQueueFree(MyCircularQueue *obj) {
    if (obj == NULL || obj->head == NULL) {
        return;
    }

    if (obj->head != NULL) {
        obj->tail->next = NULL;
        LinkedList *curr = obj->head;
        while (curr) {
            LinkedList *next = curr->next;
            free(curr);
            curr = next;
        }
    }
    free(obj);
}

int main() {
    int k = 3;
    MyCircularQueue *obj = myCircularQueueCreate(k);
    myCircularQueueEnQueue(obj, 1);
    myCircularQueueEnQueue(obj, 2);
    myCircularQueueEnQueue(obj, 3);
    myCircularQueueEnQueue(obj, 4);

    printf("rear: %d\n", myCircularQueueRear(obj));
    printf("is_full: %d\n", myCircularQueueIsFull(obj));
    printf("deque: %d\n", myCircularQueueDeQueue(obj));

    myCircularQueueEnQueue(obj, 4);
    printf("rear: %d\n", myCircularQueueRear(obj));
    return 0;
}
