#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct {
        int *data;
        int capacity;
        int head;
        int tail;
        int size;
} MyCircularQueue;

MyCircularQueue *myCircularQueueCreate(int k) {
    if (k <= 0) {
        return NULL;
    }
    MyCircularQueue *obj = malloc(sizeof(MyCircularQueue));
    if (!obj) return NULL;
    obj->data = malloc(sizeof(int) * k);
    if (!obj->data) {
        free(obj);
        return NULL;
    }
    obj->head = 0;
    obj->tail = 0;
    obj->size = 0;
    obj->capacity = k;
    return obj;
}

bool myCircularQueueEnQueue(MyCircularQueue *obj, int value) {
    if (obj->size == obj->capacity) {
        return false;
    }
    // insert element in the queue;
    obj->data[obj->tail] = value;
    obj->tail = (obj->tail + 1) % obj->capacity;
    obj->size++;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue *obj) {
    if (obj->size == 0) {
        return false;
    }
    obj->head = (obj->head + 1) % obj->capacity;
    obj->size--;
    return true;
}

int myCircularQueueFront(MyCircularQueue *obj) {
    if (obj->size == 0) {
        return -1;
    }
    return obj->data[obj->head];
}

int myCircularQueueRear(MyCircularQueue *obj) {
    if (obj->size == 0) {
        return -1;
    }
    int idx = (obj->tail - 1 + obj->capacity) % obj->capacity;
    return obj->data[idx];
}

bool myCircularQueueIsEmpty(MyCircularQueue *obj) {
    return obj->size == 0;
}

bool myCircularQueueIsFull(MyCircularQueue *obj) {
    return obj->size == obj->capacity;
}

void myCircularQueueFree(MyCircularQueue *obj) {
    if (!obj) return;
    free(obj->data);
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
